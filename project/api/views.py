from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from physical.models import PhysicalModel
from vital_signs.models import VitalSignsModel
from hospital_record.models import HospitalRecordModel
from re_examination.models import ReExaminationModel
from medical.models import MedicalModel
from .serializers import PhysicalSerializers, VitalSignsSerializers, HospitalRecordSerializers, ReExaminationSerializers, MedicalSerializers


# API FOR PHYSICAL
class PhysicalList(generics.ListCreateAPIView):
    queryset = PhysicalModel.objects.all()
    serializer_class = PhysicalSerializers

    def perform_create(self, serializer):
        serializer.save()

class PhysicalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhysicalModel.objects.all()
    serializer_class = PhysicalSerializers

    def perform_update(self, serializer):
        instance = serializer.save()

# API FOR VITAL SIGNS
class VitalSignsList(generics.ListCreateAPIView):
    queryset = VitalSignsModel.objects.all()
    serializer_class = VitalSignsSerializers

    def perform_create(self, serializer):
        serializer.save()

class VitalSignsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VitalSignsModel.objects.all()
    serializer_class = VitalSignsSerializers

    def perform_update(self, serializer):
        instance = serializer.save()

# API FOR HOSPITAL RECORD
class HospitalRecordList(generics.ListCreateAPIView):
    queryset = HospitalRecordModel.objects.all()
    serializer_class = HospitalRecordSerializers

    def perform_create(self, serializer):
        serializer.save()

class HospitalRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HospitalRecordModel.objects.all()
    serializer_class = HospitalRecordSerializers

    def perform_update(self, serializer):
        instance = serializer.save()

class UserHospitalRecord(generics.ListCreateAPIView):
    serializer_class = HospitalRecordSerializers

    def get_queryset(self):
        user_id = self.kwargs['pk']

        return HospitalRecordModel.objects.filter(user_id=user_id)

# API FOR RE EXAMINATION
class ReExaminationList(generics.ListCreateAPIView):
    serializer_class = ReExaminationSerializers

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        hospital_record_id = self.kwargs['hospital_record_id']

        return ReExaminationModel.objects.filter(hospital_record__id=hospital_record_id)

class ReExaminationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReExaminationModel.objects.all()
    serializer_class = ReExaminationSerializers

    def perform_update(self, serializer):
        instance = serializer.save()

# API FOR MEDICAL
class MedicalList(generics.ListCreateAPIView):
    queryset = MedicalModel.objects.all()
    serializer_class = MedicalSerializers

    def perform_create(self, serializer):
        serializer.save()

class MedicalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalModel.objects.all()
    serializer_class = MedicalSerializers

    def perform_update(self, serializer):
        instance = serializer.save()

