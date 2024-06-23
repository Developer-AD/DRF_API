from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Student


class UserAdmin(admin.ModelAdmin):

    list_display = ['username', 'email']  # , 'role'

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name', 'verified']

class SudentAdmin(admin.ModelAdmin):
    list_editable = ['roll', 'name', 'city']
    list_display = ['id', 'roll', 'name', 'city']
    


# admin.site.register(MyUser, UserAdmin)
# admin.site.register(Profile, ProfileAdmin)

admin.site.register(Student, SudentAdmin)

# -------------------- Another Way ---------------------------

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'roll', 'city']
# -------------------- Another Way ---------------------------