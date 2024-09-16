from django.contrib import admin

# Register your models here.
from .models import MenuItem, Highlight, Location, ItemOption, Order
from .models import Restaurant, HeaderConfig, FooterConfig, MainPageConfig, OrderItemOption


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_src', 'description')

# Inline model for OrderItem so you can add items to an order directly from the Order admin page
class OrderItemOptionInline(admin.TabularInline):
    model = OrderItemOption
    extra = 1  # Defines how many extra blank OrderItems to display by default

# Customize the OrderAdmin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_type', 'store_location', 'total_cost', 'order_time')  # Columns to display in the list view
    list_filter = ('delivery_type', 'store_location')  # Filter options in the right sidebar
    search_fields = ('store_location',)  # Add search capability by store location
    inlines = [OrderItemOptionInline]  # Include the inline form for OrderItem to edit items in an order


@admin.register(ItemOption)
class ItemOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_src', 'calories')

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'header', 'description1', 'description2', 'image_src', 'tag')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'image_src')

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
