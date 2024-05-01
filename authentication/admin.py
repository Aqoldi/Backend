from django.contrib import admin

from authentication.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in Users._meta.fields if f.name not in ["password", "last_login"]]


admin.site.register(Users, UserAdmin)
