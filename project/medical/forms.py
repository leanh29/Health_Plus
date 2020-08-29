from django import forms
from .models import MedicalModel, MedicalDetailModel

class PostMedical(forms.ModelForm):
    class Meta:
        model = MedicalModel
        fields = ['name','effect']


class PutMedical(forms.ModelForm):
    class Meta:
        model = MedicalModel
        fields = ['name','effect']

class PostMedicalDetail(forms.ModelForm):
    class Meta:
        model = MedicalDetailModel
        fields = ['medical','quantity','time']

class PutMedicalDetail(forms.ModelForm):
    class Meta:
        model = MedicalDetailModel
        fields = ['quantity','time']