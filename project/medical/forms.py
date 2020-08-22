from django import forms
from .models import MedicalModel

class PostMedical(forms.ModelForm):
    class Meta:
        model = MedicalModel
        fields = ['name','effect']


class PutMedical(forms.ModelForm):
    class Meta:
        model = MedicalModel
        fields = ['name','effect']