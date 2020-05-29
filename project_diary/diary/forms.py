from django import forms
from django.contrib.auth.models import User



class RegisterForm(forms.Form):
    username = forms.CharField(label= "Username", max_length = 12)
    email = forms.EmailField(label="Email ID")
    password = forms.CharField(label='Password', widget= forms.PasswordInput , max_length=12)
    confirm_password = forms.CharField(label='Confirm Password', widget= forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']





