from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenRefreshView

from user.models import Patient
from user.permissions import IsDoctor
from user.serializers import PatientSerializer


# Представление для входа в систему с получением JWT токена
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)  # Разрешение для всех пользователей
    serializer_class = TokenObtainPairSerializer  # Сериализатор для получения токена

    @extend_schema(
        tags=["Auth"],  # Указывает тег для документации API
        summary="Login"  # Краткое описание метода для документации
    )
    def post(self, request, *args, **kwargs):
        # Принимаем данные из запроса и проверяем их валидность
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)  # Если данные невалидны, вызываем исключение
        except TokenError:
            # Обработка ошибки токена, если токен невалидный
            return Response({"detail": "Token is invalid."}, status=401)
        # Возвращаем успешный ответ с данными токена
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


# Представление для обновления токена (refresh token)
class RefreshTokenAPIView(TokenRefreshView):
    permission_classes = (AllowAny,)  # Разрешение для всех пользователей

    @extend_schema(
        tags=["Auth"],  # Указывает тег для документации API
        summary="Refresh token"  # Краткое описание метода для документации
    )
    def post(self, request, *args, **kwargs):
        # Используем встроенный метод для обновления токена
        return super().post(request, *args, **kwargs)


# Представление для получения списка пациентов
class PatientAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)  # Требуется аутентификация и роль "DOCTOR"
    serializer_class = PatientSerializer  # Сериализатор для отображения данных пациентов
    queryset = Patient.objects.all()  # Запрос для получения всех пациентов

    @extend_schema(
        tags=["Patient"],  # Указывает тег для документации API
        summary="Get list of patients"  # Краткое описание метода для документации
    )
    def get(self, request, *args, **kwargs):
        # Обрабатываем GET-запрос для получения списка пациентов
        return super().get(request, *args, **kwargs)
