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

class PhysicalList(generics.ListCreateAPIView):
    queryset = PhysicalModel.objects.all()
    serializer_class = PhysicalSerializers

    def perform_create(self, serializer):
        serializer.save()

#@api_view(['GET', 'POST'])
# def PhysicalList(   ):
#     if request.method == 'GET':
#         physicals = PhysicalModel.objects.all()
#         serializer = PhysicalSerializers(physicals, many = True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         #print(JSONParser().parse(request)+"-----------------")
#         serializer = PhysicalSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATE)
#         return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def PhysicalDetail(request, pk):
    try:
        physical = PhysicalModel.objects.get(pk=pk)
    except PhysicalModel.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhysicalSerializers(physical)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhysicalSerializers(physical, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        physical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

