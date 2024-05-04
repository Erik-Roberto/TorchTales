from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField

from .models import CustomUser

class UserRegister(UserCreationForm):
    user_email = forms.EmailField(label= 'email')    
    first_name = forms.CharField(max_length= 30, label='first_name')
    last_name = forms.CharField(max_length= 30, label='last_name')
    user_country = CountryField(blank_label="(Select country)").formfield()
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password1',
            'password2',
        ]

class Login(forms.Form):
    username = forms.CharField(max_length= 30, required=True)
    password = forms.CharField(max_length= 30, required=True,widget=forms.PasswordInput)
