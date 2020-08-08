from django import forms
from .models import PhysicalModel

class PostPhysical(forms.ModelForm):
    class Meta:
        model = PhysicalModel
        fields = ['height', 'weight']