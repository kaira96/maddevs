from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.test import TestCase
from user.models import User


class AuthTests(TestCase):
    def setUp(self):
        # Создаем пользователя для тестирования
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()

    def test_login_success(self):
        # Генерируем JWT токен с помощью правильных данных
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_credentials(self):
        # Проверка на неправильные данные для входа
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'No active account found with the given credentials')

    def test_refresh_token_success(self):
        # Создание refresh токена
        refresh = RefreshToken.for_user(self.user)
        response = self.client.post('/api/auth/token/refresh/', {
            'refresh': str(refresh)
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_refresh_token_invalid(self):
        # Попытка обновить токен с неправильным refresh токеном
        response = self.client.post('/api/auth/token/refresh/', {
            'refresh': 'invalid_refresh_token'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Token is invalid.')

