from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics, status
from rest_framework.response import Response
from physical.models import PhysicalModel
from vital_signs.models import VitalSignsModel
from hospital_record.models import HospitalRecordModel
from .serializers import PhysicalSerializers, VitalSignsSerializers, HospitalRecordSerializers


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



