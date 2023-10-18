from django.contrib import admin
from .models import User, StudentProfile
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.register(User)


# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     ordering = ['id']
#     list_display = ['id', 'email', 'name', 'is_staff', 'phone_number', ]
#     readonly_fields = ('date_modified')
#     fieldsets = (
#         (None, {'fields': ('phone',)}),
#         ('Personal info', {'fields': ('email', 'name', 'picture', 'password',)}),
#         ('Roles', {'fields': ('is_superuser', 'is_staff',)}),
#         ('Important Dates', {'fields': ('last_login',)}),
#         ('User Verification', {'fields': ('date_modified',)}),
#
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('phone', 'name', 'password1', 'password2', 'email'),
#         }),
#     )
#     search_fields = ('email', 'phone', 'name',)
