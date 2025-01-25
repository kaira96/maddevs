from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from user.models import User, Patient


class PatientAPIViewTest(TestCase):
    def setUp(self):
        # Создаем пользователя и пациента для тестирования
        self.user_patient = User.objects.create_user(username="patient_user", password="patientpassword", user_type=1)
        self.user_doctor = User.objects.create_user(username="doctor_user", password="doctorpassword", user_type=2)

        # Сначала создаем пациентами
        self.patient = Patient.objects.create(user=self.user_patient, date_of_birth="1990-01-01",
                                              diagnoses=["Diabetes"])

        self.client = APIClient()

    def test_patient_access_as_doctor(self):
        # Получаем токен для доктора
        self.client.login(username="doctor_user", password="doctorpassword")

        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Должен быть один пациент в ответе

    def test_patient_access_as_patient(self):
        # Получаем токен для пациента
        self.client.login(username="patient_user", password="patientpassword")

        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Пациент не может получить доступ

    def test_patient_access_without_authentication(self):
        # Без аутентификации
        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

