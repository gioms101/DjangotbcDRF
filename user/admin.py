from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'address')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'address')}),
    )

