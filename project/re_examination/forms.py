from django import forms
from .models import ReExaminationModel

class PostReExamination(forms.ModelForm):
    class Meta:
        model = ReExaminationModel
        fields = ['result','date']


class PutReExamination(forms.ModelForm):
    class Meta:
        model = ReExaminationModel
        fields = ['doctor','result','date','appointment_date']

