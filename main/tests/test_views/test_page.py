
from rest_framework import status
from user.models import User

def test_pagination(self):
    # Создаем несколько пациентов
    for i in range(15):
        User.objects.create_user(username=f"user_{i}", password="password123")

    # Смотрим на 10 пациентов
    response = self.client.get('/api/patients/?page=1')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 10)  # Проверяем, что на первой странице только 10 пациентов

    # Переходим на вторую страницу
    response = self.client.get('/api/patients/?page=2')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 5)  # Проверяем, что на второй странице 5 пациентов
