from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Profile


class UserAdmin(admin.ModelAdmin):

    list_display = ['username', 'email']  # , 'role'

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name', 'verified']


admin.site.register(MyUser, UserAdmin)
admin.site.register(Profile, ProfileAdmin)