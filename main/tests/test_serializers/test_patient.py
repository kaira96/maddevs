from rest_framework.test import APITestCase
from user.models import Patient, User

from user.serializers import PatientSerializer


class PatientSerializerTests(APITestCase):

    def setUp(self):
        # Создаем пользователя (пациента)
        self.user = User.objects.create_user(username="patient", password="password")

        # Создаем пациента для тестирования
        self.patient = Patient.objects.create(user=self.user, date_of_birth="1990-01-01", diagnoses=["Flu", "Cold"])

    def test_patient_serializer_valid(self):
        """Тестируем корректную сериализацию данных пациента."""
        serializer = PatientSerializer(self.patient)
        data = serializer.data

        # Проверяем, что сериализованные данные содержат правильные поля
        self.assertEqual(set(data.keys()), {"id", "date_of_birth", "diagnoses", "created_at"})
        self.assertEqual(data["id"], self.patient.id)
        self.assertEqual(data["date_of_birth"], str(self.patient.date_of_birth))
        self.assertEqual(data["diagnoses"], self.patient.diagnoses)
        self.assertEqual(data["created_at"], self.patient.created_at.isoformat())

    def test_patient_serializer_invalid(self):
        """Тестируем сериализацию с некорректными данными."""
        invalid_data = {
            "date_of_birth": "invalid_date",  # Некорректная дата
            "diagnoses": "Cold",  # Некорректный формат диагноза
        }
        serializer = PatientSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())  # Сериализатор не должен быть валидным
        self.assertIn("date_of_birth", serializer.errors)  # Ошибка для поля "date_of_birth"
        self.assertIn("diagnoses", serializer.errors)  # Ошибка для поля "diagnoses"
