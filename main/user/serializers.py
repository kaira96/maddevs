from rest_framework import serializers

from user.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("id", "date_of_birth", "diagnoses", "created_at")
