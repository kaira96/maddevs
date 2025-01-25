from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from django.db import models

from general.models import TimeStampMixin
from user.managers import CustomUserManager


# Перечисление возможных типов пользователей
class UserType(models.IntegerChoices):
    PATIENT = 1, _("Patient")  # Пользователь типа Patient
    DOCTOR = 2, _("Doctor")  # Пользователь типа Doctor


# Кастомная модель пользователя
class User(TimeStampMixin, AbstractBaseUser, PermissionsMixin):
    # Валидатор для имени пользователя
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name=_("Username"),
        max_length=150,  # Максимальная длина имени пользователя
        unique=True,  # Уникальность имени пользователя
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],  # Применение валидатора
        error_messages={
            "unique": _("A user with that username already exists."),  # Сообщение об ошибке
        },
    )
    user_type = models.IntegerField(
        verbose_name=_("User Type"),  # Тип пользователя (Doctor или Patient)
        choices=UserType.choices,  # Варианты выбора
        default=UserType.PATIENT  # Значение по умолчанию
    )
    is_staff = models.BooleanField(
        verbose_name=_("Staff Status"),
        default=False,  # По умолчанию пользователь не является сотрудником
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,  # Пользователь активен по умолчанию
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    # Явно добавляем related_name для groups и user_permissions
    groups = models.ManyToManyField(
        to="auth.Group",
        related_name="custom_user_set",  # Уникальное имя для обратной связи
        blank=True,
        help_text=_("The groups this user belongs to."),
        verbose_name=_("groups"),
    )
    user_permissions = models.ManyToManyField(
        to="auth.Permission",
        related_name="custom_user_permissions_set",  # Уникальное имя для обратной связи
        blank=True,
        help_text=_("Specific permissions for this user."),
        verbose_name=_("user permissions"),
    )
    objects = CustomUserManager()  # Устанавливаем менеджер для модели

    USERNAME_FIELD = "username"  # Поле, используемое для входа
    REQUIRED_FIELDS = []  # Список обязательных полей

    def __str__(self):
        return self.username  # Отображение имени пользователя

    class Meta:
        db_table = 'users'  # Имя таблицы в базе данных
        verbose_name = 'user'  # Название модели в админке
        verbose_name_plural = 'users'  # Множественное число для названия модели


# Модель пациента
class Patient(TimeStampMixin):
    user = models.ForeignKey(
        to=User,  # Связь с моделью User
        on_delete=models.CASCADE,  # Удаление пациента при удалении пользователя
        related_name='patiens',  # Связанное имя для обратного доступа
        verbose_name=_('User')  # Название поля в админке
    )
    date_of_birth = models.DateField()  # Дата рождения пациента
    diagnoses = ArrayField(base_field=models.CharField(max_length=100))  # Массив диагнозов

    class Meta:
        db_table = 'patients'  # Имя таблицы в базе данных
        verbose_name = 'patient'  # Название модели в админке
        verbose_name_plural = 'patients'  # Множественное число для названия модели
