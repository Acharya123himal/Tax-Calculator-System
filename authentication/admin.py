from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields=('username','email','first_name','last_name','is_active','is_staff','is_blocked')
    ordering=('username',)
    list_display=('email','username','first_name','last_name','is_active','is_staff')
    
admin.site.register(User,UserAdminConfig)