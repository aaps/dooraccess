from django.contrib import admin
from models import CustomUser
# from models import User
from models import Event
from forms import CustomUserCreationForm



class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm


class EventAdmin(admin.ModelAdmin):
    pass


# admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)

