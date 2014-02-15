from django import forms
from models import CustomUser
from models import LogEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from datetime import date
from django.forms import widgets
from django.forms import extras
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.utils.translation import ugettext, ugettext_lazy as _
import pdb
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms.util import ErrorList


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        

class CustomUserChangeForm(UserChangeForm):
    
    # doorkey = forms.CharField(label='Doorkey')
    # image  = forms.FileField()
    # last_key = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        # lastlog = LogEntry.objects.order_by('-id')[0]
        # pdb.set_trace()
        obj = super(CustomUserChangeForm, self).save(commit=False)
        self.fields['doorkey'].initial = obj.doorkey
        self.fields['image'].initial = obj.image
        # self.fields['last_key'].widget.attrs['readonly'] = True
        # self.fields['last_key'].initial = 'ladida'
        

    def save(self, commit=True):
        obj = super(CustomUserChangeForm, self).save(commit=False)
        self.fields['doorkey'].error_messages['myerror'] = 'The important message'
        # raise forms.ValidationError(self.fields['doorkey'].error_messages['myerror'])
        obj.doorkey = self.cleaned_data['doorkey']
        obj.image = self.cleaned_data['image']
        obj.save()
        return obj

    def clean(self):
        cleaned_data = self.cleaned_data
        # self._errors['doorkey'] = ErrorList()
        # if CustomUser.objects.filter(doorkey = cleaned_data['doorkey']).exists():
            # self._errors['doorkey'].append('must be louder!')
            # raise forms.ValidationError("You have failed validation!")
        # raise ValidationError({'doorkey': ["Arg !!!",]})
        return cleaned_data


    class Meta(UserChangeForm.Meta):
        model = CustomUser
        # js = (
        #     '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
        #     )
        # fields =  ('last_key','is_active')
        # readonly_fields = ['last_key',]


class LogEntryCreationForm(forms.ModelForm):
    
    doorkey = forms.CharField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )

    time = forms.DateTimeField(
        widget=extras.SelectDateWidget(attrs={'readonly':'readonly'})
    )

    valid = forms.BooleanField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )

    class Meta:
        model = CustomUser

class LogEntryChangeForm(forms.ModelForm):


    # doorkey = forms.CharField(
    #     widget=forms.TextInput(attrs={'readonly':'readonly'})
    # )

    # name = forms.CharField(
    #     widget=forms.TextInput(attrs={'readonly':'readonly'})
    # )

    # time = forms.DateTimeField(
    #     widget=extras.SelectDateWidget(attrs={'readonly':'readonly'})
    # )

    # valid = forms.BooleanField(
    #     widget=forms.TextInput(attrs={'readonly':'readonly'})
    # )
    
    # forms.fields['valid'].widget.attrs['readonly'] = True

    class Meta:
        model = CustomUser
        # readonly_fields = ['valid','doorkey']


