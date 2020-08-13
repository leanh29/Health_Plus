from rest_framework import serializers
from Measure.models import Measure
from physical.models import PhysicalModel
from user.models import User

class MeasureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['chieucao', 'cannang']

class PhysicalSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysicalModel
        fields = ['id','height','weight','date','user']

class UserSerializers(serializers.ModelSerializer):
    user_physical = PhysicalSerializers(many = True)
    class Meta:
        model = User





        