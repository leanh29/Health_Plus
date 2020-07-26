from rest_framework import serializers
from Measure.models import Measure

class MeasureSerializers(serializers.ModelSerializer):

    class Meta:
        model = Measure
        fields = ['chieucao', 'cannang']
        