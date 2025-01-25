from rest_framework.permissions import BasePermission

from user.models import UserType


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == UserType.DOCTOR
