from rest_framework import serializers
from user.models import Patient

# Сериализатор для модели Patient
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        # Указываем модель, которую сериализуем, и поля для включения в сериализованный вывод
        model = Patient
        fields = ("id", "date_of_birth", "diagnoses", "created_at")
