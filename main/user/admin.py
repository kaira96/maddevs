from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User, Patient


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (
            None,
            {"fields": ["username", "user_type", "password"]}
        ),
        (
            "Permissions",
            {"fields": ["is_staff", "is_superuser"]}
        ),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ["username", "user_type", "password1", "password2"]}
        ),
        (
            "Permissions",
            {"fields": ["is_staff", "is_superuser"]}
        ),
    )
    list_display = [
        "id",
        "username",
        "user_type",
    ]
    search_fields = [
        "id",
        "username",
    ]
    list_filter = ["user_type"]

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date_of_birth', 'created_at']

admin.site.unregister(Group)
