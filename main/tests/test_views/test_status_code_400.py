
from rest_framework import status


def test_invalid_data(self):
    # Проверим, что при отправке некорректных данных получим статус 400
    response = self.client.post('/api/auth/login/', {
        'username': 'testuser',  # Нет пароля
    })
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertIn('password', response.data)  # Ошибка валидации для пароля
