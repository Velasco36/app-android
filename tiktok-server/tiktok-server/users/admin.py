from django.contrib import admin

from .models import *

#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.utils.translation import gettext_lazy as _

admin.site.register(User)

"""
@admin.register(User)

class UserAdmin(BaseUserAdmin):
    list_display= ['email',  'username', 'first_name',
                   'last_name' 'is_staff', 'date_joined' ]
    
    fieldsets = (
        (None, {'fields': ('username', 'passowrd')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'email')}),
        (_('Permissions'),{
            'fields': ('is_activate', 'is_staff', 'is_superuser', 'groups', 'user_prmissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    readonly_fields = ['date_joined', 'last_login']
"""