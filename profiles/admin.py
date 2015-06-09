from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile

class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInlineAdmin]

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)