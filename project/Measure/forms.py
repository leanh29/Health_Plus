from django import forms
from .models import Measure

class MeasureCreationForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = ['chieucao', 'cannang']

class MeasureUpdateForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = ['chieucao', 'cannang' ]