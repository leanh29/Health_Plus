from django import forms
from .models import PhysicalModel

class PostPhysical(forms.ModelForm):
    height = forms.CharField(widget= forms.TextInput
                           (attrs={'class':'numberinput form-control'}))

    class Meta:
        model = PhysicalModel
        fields = ['height', 'weight','date','user']


class PutPhysical(forms.ModelForm):
    class Meta:
        model = PhysicalModel
        fields = ['height', 'weight','date','user']