from rest_framework import serializers
from physical.models import PhysicalModel
from vital_signs.models import VitalSignsModel
from hospital_record.models import HospitalRecordModel
from re_examination.models import ReExaminationModel
from medical.models import MedicalModel, MedicalDetailModel
from news.models import NewsModel
from user.models import User

# PHYSICAL 
class PhysicalSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysicalModel
        fields = ['id','height','weight','date','user']

# class FilterPhysicalSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = PhysicalModel
#         fields = ['id','height','weight','date','user']

#     def get_data(self, obj):
#         names = self.context['request'].query_params.get('height', None)
#         data = PhysicalModel.objects.filter(height=names.split(','))
#         data_serializer = MyDataSerializer(data, many=True)
#         return data_serializer.data

#         queryset = PhysicalModel.objects.all()
#         height = self.request.query_params.get('height', None)
#         if height is not None:
#             queryset = queryset.filter(height=height)

# VITAL SIGNS
class VitalSignsSerializers(serializers.ModelSerializer):
    class Meta:
        model = VitalSignsModel
        fields = ['id','temperature','bool_pressure','heartbeat','breathing','time','user']


# RE EXAMINATION
class ReExaminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReExaminationModel
        fields = ['id', 'doctor', 'result', 'date','appointment_date', 'hospital_record']

# HOSPITAL RECORD
class HospitalRecordSerializers(serializers.ModelSerializer):
    # hr_re_examination = ReExaminationSerializers(many=True)
    class Meta:
        model = HospitalRecordModel
        # fields = ['id', 'hospital', 'disease', 'start_time','status', 'user']
        fields = '__all__'

# USER
class UserSerializers(serializers.ModelSerializer):
    user_physical = PhysicalSerializers(many = True)
    user_vital_signs = VitalSignsSerializers(many=True)
    user_hospital_record = HospitalRecordSerializers(many=True)
    class Meta:
        model = User

# MEDICAL 
class MedicalSerializers(serializers.ModelSerializer):
    #medical_prescription = MedicalDetailModel(many=True)
    class Meta:
        model = MedicalModel
        fields = '__all__'

# MEDICAL DETAIL
class MedicalDetailSerializersGet(serializers.ModelSerializer):
    # quantity = serializers.ReadOnlyField()
    # time = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    effect = serializers.ReadOnlyField()
    re_examination_id = serializers.ReadOnlyField()
    medical_id = serializers.ReadOnlyField()
    medical_detail_id = serializers.ReadOnlyField()

    class Meta:
        #model = MedicalModel
        model = MedicalDetailModel
        fields = '__all__'

class MedicalDetailSerializersPost(serializers.ModelSerializer):
    # quantity = serializers.ReadOnlyField()
    # time = serializers.ReadOnlyField()
    # name = serializers.ReadOnlyField()
    # effect = serializers.ReadOnlyField()
    # re_examination = serializers.ReadOnlyField()
    # medical = serializers.ReadOnlyField()

    class Meta:
        #model = MedicalModel
        model = MedicalDetailModel
        fields = '__all__'

# USER
class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'