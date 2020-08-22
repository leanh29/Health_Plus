from rest_framework import serializers
from .models import MedicalModel

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalModel