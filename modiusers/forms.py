from django import forms
from models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.utils.translation import ugettext, ugettext_lazy as _
import pdb


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        

class CustomUserChangeForm(UserChangeForm):
    
    doorkey = forms.CharField(label='Doorkey')
    image  = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        obj = super(CustomUserChangeForm, self).save(commit=False)
        self.fields['doorkey'].initial = obj.doorkey
        self.fields['image'].initial = obj.image
        

    def save(self, commit=True):
        obj = super(CustomUserChangeForm, self).save(commit=False)
        obj.doorkey = self.cleaned_data['doorkey']
        obj.image = self.cleaned_data['image']
        obj.save()
        return obj


        # user = super(CustomUserChangeForm, self).save(commit=False)


    # def __init__(self, *args, **kwargs):
    #     super(CustomUserChangeForm, self).__init__(*args, **kwargs)
    #     del self.fields['first_name'] # This is a declared field we really want to be removed


    class Meta:
        model = CustomUser
        # fields = ['doorkey', 'image']

