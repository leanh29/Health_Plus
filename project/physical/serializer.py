from rest_framework import serializers
from .models import PhysicalModel

class PhysicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalModel
        