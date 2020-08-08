from rest_framework import serializers
from Measure.models import Measure
from physical.models import PhysicalModel

class MeasureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['chieucao', 'cannang']

class PhysicalSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysicalModel
        fields = ['height','weight']

    # def create(self, validated_data):
    #     return PhysicalModel.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.height = validated_data.get('height', instance.height)
    #     instance.weight = validated_data.get('weight', instance.weight)
    #     return instance


        