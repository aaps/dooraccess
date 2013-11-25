from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from models import CustomUser
from django import forms

class SignUpForm(UserCreationForm):
    """ Require email address when a user signs up """
    email = forms.EmailField(label='Email address', max_length=75)
    doorkey = forms.EmailField(label='Email address', max_length=75)
    
    class Meta:
        model = CustomUser
        fields = ('doorkey') 

