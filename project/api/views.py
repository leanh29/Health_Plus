import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics, status
from rest_framework.response import Response
#from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from physical.models import PhysicalModel
from vital_signs.models import VitalSignsModel
from hospital_record.models import HospitalRecordModel
from re_examination.models import ReExaminationModel
from medical.models import MedicalModel, MedicalDetailModel
from .serializers import PhysicalSerializers, VitalSignsSerializers, HospitalRecordSerializers, ReExaminationSerializers, MedicalSerializers, MedicalDetailSerializersGet, MedicalDetailSerializersPost


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

class UserPhysical(generics.ListCreateAPIView):
    serializer_class = PhysicalSerializers

    def get_queryset(self):
        user_id = self.kwargs['pk']

        return PhysicalModel.objects.filter(user_id=user_id)

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

class UserVitalSigns(generics.ListCreateAPIView):
    serializer_class = VitalSignsSerializers

    def get_queryset(self):
        user_id = self.kwargs['pk']

        return VitalSignsModel.objects.filter(user_id=user_id)


# ---------------------------------------------------API FOR HOSPITAL RECORD------------------------------
class HospitalRecordList(generics.ListCreateAPIView):
    queryset = HospitalRecordModel.objects.all()
    serializer_class = HospitalRecordSerializers
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['hospital', 'disease']

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


# ----------------------------------------------------API FOR RE EXAMINATION------------------------------
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

# API FOR MEDICAL DETAIL
# class MedicalDetailListtt(generics.ListCreateAPIView):
#     serializer_class = MedicalDetailSerializers

#     def perform_create(self, serializer):
#         serializer.save()

#     def get_queryset(self, re_examination_id=12):
#         if re_examination_id:
#             print("-----------------"+str(re_examination_id))
#             sql ="""
#             SELECT
#                 m.id,
#                 m.name,
#                 m.effect,
#                 md.quantity,
#                 md.time
#             FROM
#                 medical_medicalmodel m
#                 LEFT JOIN
#                 (
#                     SELECT
#                         medical_id,
#                         quantity,
#                         time
#                     FROM
#                         medical_medicaldetailmodel
#                     WHERE
#                         re_examination_id = {}
#                 ) md
#                 ON m.id = md.medical_id
#             ORDER BY
#                 m.name
#             """.format(re_examination_id)
#         else:
#             print("---------------sssssssss--"+str(re_examination_id))
#             sql = """
#                 SELECT
#                     id,
#                     name,
#                     effect,
#                     0 as quantity,
#                     0 as time
#                 FROM
#                     medical_medicalmodel
#                 ORDER BY
#                     name
#             """

#         return MedicalModel.objects.raw(sql)

class MedicalDetailGet(generics.ListCreateAPIView):
    # serializer_class = MedicalDetailSerializers

    # def get_queryset(self):
    #     re_examination_id = self.kwargs['re_examination_id']

    #     return MedicalDetailModel.objects.filter(re_examination_id=re_examination_id)

    serializer_class = MedicalDetailSerializersGet

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self, re_examination_id=2):
        #if re_examination_id:
        re_examination_id = self.kwargs['re_examination_id']
        print("-----------------"+str(re_examination_id))
        sql ="""
        SELECT
            m.id,
            m.name,
            m.effect,
            md.id as medical_detail_id,
            md.quantity,
            md.time,
            re_examination_id,
            md.medical_id
        FROM
            medical_medicalmodel m
            INNER JOIN
            (
                SELECT
                    id,
                    medical_id,
                    quantity,
                    time,
                    re_examination_id
                FROM
                    medical_medicaldetailmodel
                WHERE
                    re_examination_id = {}
            ) md
            ON m.id = md.medical_id
        ORDER BY
            m.name
        """.format(re_examination_id)

        print("-----------------"+sql)
        b = {
            'b': 123
        }
        a = {}
        a = MedicalDetailModel.objects.raw(sql)

        #return JsonResponse(list(a), safe = False)
        return MedicalDetailModel.objects.raw(sql)

class MedicalDetailPost(generics.ListCreateAPIView):
    serializer_class = MedicalDetailSerializersPost

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        re_examination_id = self.kwargs['re_examination_id']

        return MedicalDetailModel.objects.filter(re_examination_id=re_examination_id)

class MedicalDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalDetailModel.objects.all()
    serializer_class = MedicalDetailSerializersPost

    def perform_update(self, serializer):
        instance = serializer.save()