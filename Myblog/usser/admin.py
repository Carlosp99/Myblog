from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUseradmin
from usser.models import User

@admin.register(User)
class UserAdmin(BaseUseradmin):
    pass
