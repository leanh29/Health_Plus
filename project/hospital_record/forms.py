from django import forms
from .models import HospitalRecordModel

class PostHospitalRecord(forms.ModelForm):
    class Meta:
        model = HospitalRecordModel
        fields = ['hospital','user']


class PutHospitalRecord(forms.ModelForm):
    class Meta:
        model = HospitalRecordModel
        fields = ['hospital','user']