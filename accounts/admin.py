from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        'email',
        'username',
        'age',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + (('Extra',{'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age',)}),)
    
admin.site.register(CustomUser, CustomUserAdmin)