from rest_framework import serializers
from .models import ReExaminationModel

class ReExeminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReExaminationModel