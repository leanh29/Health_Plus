from django import forms
from .models import PhysicalModel


class PostPhysical(forms.ModelForm):
    # user = forms.CharField()

    class Meta:
        model = PhysicalModel
        fields = ['height', 'weight', 'date', 'user']


class PutPhysical(forms.ModelForm):
    class Meta:
        model = PhysicalModel
        fields = ['height', 'weight', 'date', 'user']

# user = forms.IntegerField(widget= forms.TextInput
# (attrs={'class':'numberinput form-control'}))
