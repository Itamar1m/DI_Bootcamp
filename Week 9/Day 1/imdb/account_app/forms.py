from django.contrib.auth.models import User
from django import forms


class Login_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
        'password': forms.PasswordInput(),
        }