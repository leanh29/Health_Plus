from django import forms


class PostSymptom(forms.Form):
    symptom = forms.CharField(label='symptom', max_length=100)
    height = forms.IntegerField(label='height')
    weight = forms.IntegerField(label='weight')
