from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

from general.models import TimeStampMixin
from user.managers import CustomUserManager


class UserType(models.IntegerChoices):
    PATIENT = 1, _("Patient")
    DOCTOR = 2, _("Doctor")


class User(TimeStampMixin, AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name=_("Username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    user_type = models.IntegerField(
        verbose_name=_("User Type"),
        choices=UserType.choices,
        default=UserType.PATIENT
    )
    is_staff = models.BooleanField(
        verbose_name=_("Staff Status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Patient(TimeStampMixin):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='patients',
        verbose_name=_('User')
    )
    date_of_birth = models.DateField()
    diagnoses = ArrayField(base_field=models.CharField(max_length=100))

    class Meta:
        db_table = 'patients'
        verbose_name = 'patient'
        verbose_name_plural = 'patients'
