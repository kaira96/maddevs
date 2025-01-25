
from rest_framework import status
from user.models import User, Patient


def test_filtering(self):
    # Создаем пациентов с разными диагнозами
    patient1 = Patient.objects.create(user=self.user_patient, date_of_birth="1990-01-01", diagnoses=["Diabetes"])
    patient2 = Patient.objects.create(user=self.user_patient, date_of_birth="1992-02-02", diagnoses=["Asthma"])

    # Фильтруем по диагнозу
    response = self.client.get('/api/patients/', {'diagnoses': 'Diabetes'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)  # Должен быть только один пациент с диагнозом "Diabetes"
