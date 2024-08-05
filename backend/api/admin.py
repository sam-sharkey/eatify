from django.contrib import admin

# Register your models here.
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_src', 'description')