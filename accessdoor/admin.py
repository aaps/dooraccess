from django.contrib import admin
from django import forms
from models import CustomUser
from models import User
from models import Event
from django.forms import ModelForm, PasswordInput



class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser




class CustomUserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm


class EventAdmin(admin.ModelAdmin):
		pass




admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)
