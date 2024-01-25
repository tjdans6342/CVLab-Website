from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# User
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += ('Custom fields', {
        'fields': ('nickname', 'profile_pic', 'intro', 'rank',)
    }
),