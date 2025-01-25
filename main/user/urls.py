from django.urls import path
from user.views import PatientAPIView, LoginAPIView, RefreshTokenAPIView

app_name = 'user'

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("refresh/", RefreshTokenAPIView.as_view(), name="refresh-token"),
    path('patients/', PatientAPIView.as_view(), name='patients'),
]
