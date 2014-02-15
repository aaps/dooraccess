from django.contrib import admin
from models import CustomUser
from models import LogEntry
from forms import CustomUserCreationForm
from forms import CustomUserChangeForm
from forms import LogEntryChangeForm
from forms import LogEntryCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _





class CustomUserAdmin(UserAdmin):

    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
    list_display = ('username', 'doorkey')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
                # (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                # (_('Permissions'), {'fields': perm_fields}),
                (_('Extra'), {'fields': ('doorkey','image','is_active')})
                # (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )



class LogEntryAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return False

    form = LogEntryChangeForm
    add_form = LogEntryCreationForm

    readonly_fields = ['name','time','doorkey','validentry']

    list_display = ('name', 'time')




admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
