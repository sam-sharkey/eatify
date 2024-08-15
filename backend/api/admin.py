from django.contrib import admin

# Register your models here.
from .models import MenuItem, Highlight
from .models import Restaurant, HeaderConfig, FooterConfig, MainPageConfig


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_src', 'description')


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'header', 'description1', 'description2', 'image_src', 'tag')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name',)
    filter_horizontal = ('users', )


@admin.register(HeaderConfig)
class HeaderConfigAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'left_header_items', 'right_header_items', 'custom_css')
    search_fields = ('restaurant__name', 'left_header_items', 'right_header_items')
    list_filter = ('restaurant',)

@admin.register(FooterConfig)
class FooterConfigAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'links_visible', 'app_download_visible', 'newsletter_visible', 'custom_css')
    search_fields = ('restaurant__name',)
    list_filter = ('restaurant', 'links_visible', 'app_download_visible', 'newsletter_visible')

@admin.register(MainPageConfig)
class MainPageConfigAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'highlights_visible', 'menu_visible', 'feature_visible', 'news_visible', 'custom_css', 'css_variables')
    search_fields = ('restaurant__name',)
    list_filter = ('restaurant', 'highlights_visible', 'menu_visible', 'feature_visible', 'news_visible')
