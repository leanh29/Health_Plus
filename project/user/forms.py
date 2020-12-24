from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import ProfileModel

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email' ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image' ]