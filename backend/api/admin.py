from django.contrib import admin

# Register your models here.
from .models import MenuItem, Highlight


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_src', 'description')
    

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ('header_line', 'body', 'background_image')