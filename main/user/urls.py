from django.urls import path

from user.views import LoginView, PatientsView

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('patients/', PatientsView.as_view(), name='patients'),
]