from socket import fromshare
from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from .models import Users

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        widgets = {
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail address'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-entry password'})

    

    