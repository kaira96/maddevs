from django.test import TestCase
from user.models import Patient, User


class PatientModelTest(TestCase):
    def setUp(self):
        # Создаем пользователя, чтобы связать его с пациентом
        self.user = User.objects.create_user(username="john_doe", password="password123")

    def test_patient_creation(self):
        # Создаем пациента и проверяем, что все поля заполнены корректно
        patient = Patient.objects.create(user=self.user, date_of_birth="1990-01-01", diagnoses=["Diabetes", "Asthma"])
        self.assertEqual(patient.user.username, "john_doe")
        self.assertEqual(patient.date_of_birth, "1990-01-01")
        self.assertEqual(patient.diagnoses, ["Diabetes", "Asthma"])

    def test_patient_str_method(self):
        patient = Patient.objects.create(user=self.user, date_of_birth="1990-01-01", diagnoses=["Diabetes"])
        # Можно добавить метод __str__ в модель Patient, например:
        # def __str__(self):
        #     return f"{self.user.username} - {self.diagnoses}"
        self.assertEqual(str(patient), "john_doe - ['Diabetes']")

    def test_patient_user_relationship(self):
        # Проверим связь между пользователем и пациентом
        patient = Patient.objects.create(user=self.user, date_of_birth="1990-01-01", diagnoses=["Diabetes"])
        self.assertEqual(self.user.patiens.count(), 1)  # Проверяем, что у пользователя есть 1 пациент

    def test_foreign_key_constraint(self):
        # Проверим, что удаление пользователя приведет к удалению пациента
        patient = Patient.objects.create(user=self.user, date_of_birth="1990-01-01", diagnoses=["Diabetes"])
        user_id = self.user.id
        self.user.delete()
        # Попробуем найти пациента по id, должен быть исключение
        with self.assertRaises(Patient.DoesNotExist):
            Patient.objects.get(id=patient.id)
