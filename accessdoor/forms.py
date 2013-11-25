from django import forms
from models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, Form, PasswordInput


class CustomUserCreationForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].required = True
    #     self.fields['first_name'].required = True
    #     self.fields['last_name'].required = True


    class Meta:
        model = CustomUser


    # password = forms.CharField(widget=forms.PasswordInput())
    # testings = forms.CharField(max_length=100)
    # class Meta:
    #     model = CustomUser
    #     fields = ['password', 'key', 'testings']
    #     exclude = ('first_name',)


# form = UserCreationForm()