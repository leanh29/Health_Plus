from rest_framework import serializers
from .models import VitalSignsModel

class VitalSignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSignsModel