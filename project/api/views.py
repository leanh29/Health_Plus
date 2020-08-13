from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MeasureSerializers
from Measure.models import Measure
from physical.models import PhysicalModel
from .serializers import PhysicalSerializers
from django.views.decorators.csrf import csrf_exempt
#from rest_framework import APIView

class CreateView(generics.ListCreateAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializers

    def perform_create(self, serializer):
        serializer.save()

class DeatailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializers

    def perform_update(self, serializer):
        instance = serializer.save()
        #send_email_confirmation(user=self.request.user, modified=instance)

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



