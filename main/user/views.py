from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.models import PatientModel


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if not user:
            raise AuthenticationFailed("Invalid username or password")

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class PatientsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.groups.filter(name='doctor').exists():
            raise PermissionDenied("You do not have permission to access this resource.")

        patients = PatientModel.objects.all()
        serialized_patients = [
            {
                'id': patient.id,
                'date_of_birth': patient.date_of_birth,
                'diagnoses': patient.diagnoses,
                'created_at': patient.created_at,
            }
            for patient in patients
        ]
        return Response(serialized_patients)
