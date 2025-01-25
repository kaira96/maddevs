from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from user.models import User, UserType


class IsDoctorPermissionTests(APITestCase):

    def setUp(self):
        # Создаем пользователей с разными типами
        self.doctor = User.objects.create_user(username="doctor_user", password="password", user_type=UserType.DOCTOR)
        self.patient = User.objects.create_user(username="patient_user", password="password",
                                                user_type=UserType.PATIENT)

        # Создаем URL для тестируемого API
        self.url = reverse("patient-list")  # Замените на ваш URL для проверки прав доступа

    def test_doctor_access(self):
        """Проверка доступа для пользователя типа DOCTOR"""
        # Аутентификация как доктор
        self.client.login(username="doctor_user", password="password")

        # Запрос на доступ
        response = self.client.get(self.url)

        # Проверка, что доктор имеет доступ
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patient_access(self):
        """Проверка отказа в доступе для пользователя типа PATIENT"""
        # Аутентификация как пациент
        self.client.login(username="patient_user", password="password")

        # Запрос на доступ
        response = self.client.get(self.url)

        # Проверка, что пациент не имеет доступа
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_access(self):
        """Проверка отказа в доступе для неавторизованного пользователя"""
        response = self.client.get(self.url)

        # Проверка, что неавторизованный пользователь не имеет доступа
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
