from datetime import date, datetime
from typing import TypedDict
from django.db import models

class PatientModel(models.Model):
    date_of_birth = models.DateField()
    diagnoses = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class Patient(TypedDict):
    id: int
    date_of_birth: date
    diagnoses: list[str]
    created_at: datetime