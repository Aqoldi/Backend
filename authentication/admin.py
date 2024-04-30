from django.contrib import admin
from authentication.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    
admin.site.register(User, UserAdmin)