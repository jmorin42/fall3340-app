from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Task
admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "first_name", "last_name", "email", "password"]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Task)