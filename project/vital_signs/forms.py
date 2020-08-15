from django import forms
from .models import VitalSignsModel

class PostVitalSigns(forms.ModelForm):
    class Meta:
        model = VitalSignsModel
        fields = ['temperature', 'bool_pressure','heartbeat','breathing','user']


class PutVitalSigns(forms.ModelForm):
    class Meta:
        model = VitalSignsModel
        fields = ['temperature', 'bool_pressure','heartbeat','breathing','user']