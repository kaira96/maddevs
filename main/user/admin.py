from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User, Patient

# Регистрация кастомного UserAdmin с дополнительными полями
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Поля, отображаемые при редактировании пользователя
    fieldsets = (
        (
            None,
            {"fields": ["username", "user_type", "password"]}  # Основные поля пользователя
        ),
        (
            "Permissions",
            {"fields": ["is_staff", "is_superuser"]}  # Поля прав доступа
        ),
    )
    # Поля, отображаемые при добавлении нового пользователя
    add_fieldsets = (
        (
            None,
            {"fields": ["username", "user_type", "password1", "password2"]}  # Поля регистрации
        ),
        (
            "Permissions",
            {"fields": ["is_staff", "is_superuser"]}  # Поля прав доступа
        ),
    )
    # Поля, отображаемые в списке пользователей
    list_display = [
        "id",           # ID пользователя
        "username",     # Имя пользователя
        "user_type",    # Тип пользователя (например, doctor, patient и т.д.)
    ]
    # Поля для поиска в админке
    search_fields = [
        "id",
        "username",
    ]
    # Фильтр для пользователей по user_type
    list_filter = ["user_type"]

# Регистрация модели Patient в админке
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    # Поля, отображаемые в списке пациентов
    list_display = ['id', 'user', 'date_of_birth', 'created_at']  # Включает ID, пользователя, дату рождения и дату создания записи

# Удаление группы из админки, если она не используется
admin.site.unregister(Group)