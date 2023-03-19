from django.contrib import admin
from . import models



@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    # list_filter = ('is_staff', 'is_active', 'is_superuser')
    # ordering = ('-date_joined',