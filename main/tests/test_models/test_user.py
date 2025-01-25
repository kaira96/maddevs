from django.test import TestCase
from user.models import User, UserType
from django.core.exceptions import ValidationError


class UserModelTest(TestCase):
    def test_user_creation(self):
        # Проверим создание пользователя с обычным типом
        user = User.objects.create_user(username="john_doe", password="password123")
        self.assertEqual(user.username, "john_doe")
        self.assertTrue(user.check_password("password123"))
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

        # Проверим создание суперпользователя
        superuser = User.objects.create_superuser(username="admin", password="adminpassword")
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_user_type_default(self):
        # Проверим, что тип пользователя по умолчанию — PATIENT
        user = User.objects.create_user(username="patient_user", password="password123")
        self.assertEqual(user.user_type, UserType.PATIENT)

    def test_unique_username(self):
        # Проверим, что уникальность username работает
        User.objects.create_user(username="unique_user", password="password123")
        with self.assertRaises(ValidationError):
            User.objects.create_user(username="unique_user", password="anotherpassword")

    def test_user_str_method(self):
        user = User.objects.create_user(username="str_user", password="password123")
        self.assertEqual(str(user), "str_user")

