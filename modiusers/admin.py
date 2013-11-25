from django.contrib import admin
from models import CustomUser
from forms import CustomUserCreationForm
from forms import CustomUserChangeForm
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



    # def get_fieldsets(self, request, obj=None):
    #     if not obj:
    #         return self.add_fieldsets

    #     return [(None, {'fields': ('username', 'password')}),
    #             # (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    #             # (_('Permissions'), {'fields': perm_fields}),
    #             (_('Extra'), {'fields': ('doorkey','image')})
    #             # (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    #             ]


admin.site.register(CustomUser, CustomUserAdmin)