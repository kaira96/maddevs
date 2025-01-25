from rest_framework.permissions import BasePermission
from user.models import UserType

# Класс проверки прав доступа для пользователей с типом "DOCTOR"
class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        # Проверка, является ли тип пользователя на основе запроса DOCTOR
        return request.user.user_type == UserType.DOCTOR