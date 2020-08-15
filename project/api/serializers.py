from rest_framework import serializers
from Measure.models import Measure
from physical.models import PhysicalModel
from vital_signs.models import VitalSignsModel
from user.models import User

class MeasureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['chieucao', 'cannang']

class PhysicalSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysicalModel
        fields = ['id','height','weight','date','user']

class VitalSignsSerializers(serializers.ModelSerializer):
    class Meta:
        model = VitalSignsModel
        fields = ['id','temperature','bool_pressure','heartbeat','breathing','time','user']

class VitalSignsSerializers(serializers.ModelSerializer):
    class Meta:
        model = VitalSignsModel
        fields = ['id','temperature','bool_pressure','heartbeat','breathing','time','user']

class UserSerializers(serializers.ModelSerializer):
    user_physical = PhysicalSerializers(many = True)
    user_vital_signs = VitalSignsSerializers(many=True)
    class Meta:
        model = User






        