from django.shortcuts import render
from rest_framework import generics
from .serializers import MeasureSerializers
from Measure.models import Measure

class CreateView(generics.ListCreateAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializers

    def perform_create(self, serializer):
        serializer.save()

class DeatailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializers