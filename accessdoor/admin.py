from django.contrib import admin
from models import CustomUser
from models import Event

# class CustomUserInline(admin.StackedInline):
#     model = CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
		pass
		# inlines = [CustomUserInline]



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)
