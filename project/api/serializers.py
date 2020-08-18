from rest_framework import serializers
from physical.models import PhysicalModel
from vital_signs.models import VitalSignsModel
from hospital_record.models import HospitalRecordModel
from user.models import User

# PHYSICAL 
class PhysicalSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysicalModel
        fields = ['id','height','weight','date','user']

# VITAL SIGNS
class VitalSignsSerializers(serializers.ModelSerializer):
    class Meta:
        model = VitalSignsModel
        fields = ['id','temperature','bool_pressure','heartbeat','breathing','time','user']

# HOSPITAL RECORD
class HospitalRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = HospitalRecordModel
        fields = ['id', 'hospital', 'disease', 'start_time','status', 'user']

# USER
class UserSerializers(serializers.ModelSerializer):
    user_physical = PhysicalSerializers(many = True)
    user_vital_signs = VitalSignsSerializers(many=True)
    user_hospital_record = HospitalRecordSerializers(many=True)
    class Meta:
        model = User






        