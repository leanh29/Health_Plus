from rest_framework import serializers
from .models import HospitalRecordModel

class HospitalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalRecordModel