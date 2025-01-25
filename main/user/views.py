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


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer

    @extend_schema(
        tags=["Auth"],
        summary="Login"
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError:
            return Response({"detail": "Token is invalid."}, status=401)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RefreshTokenAPIView(TokenRefreshView):
    permission_classes = (AllowAny,)

    @extend_schema(
        tags=["Auth"],
        summary="Refresh token"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class PatientAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    @extend_schema(
        tags=["Patient"],
        summary="Get list of patients"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
