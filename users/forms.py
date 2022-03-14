from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class UserForm(UserCreationForm):
    address = forms.CharField()
    phone_number = forms.IntegerField()
    email = forms.EmailField()
    class Meta:
            model = User
            fields = ('email', 'phone_number', 'email', 'password1' ,'password2' )