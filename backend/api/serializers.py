from rest_framework import serializers
from .models import MenuItem, Highlight, Restaurant, HeaderConfig, FooterConfig, MainPageConfig, Location, ItemOption

class ItemOptionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOption
        fields = ['id', 'name']

class MenuItemSerializer(serializers.ModelSerializer):
    options = ItemOptionNameSerializer(many=True, read_only=True)
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'classification', 'price', 'calories', 'image_src', 'allergens', 'tag', 'options']

class ItemOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOption
        fields = ['id', 'image_src', 'name', 'calories', 'cost', 'classification', 'is_in_stock']


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = ['title', 'header', 'description1', 'description2', 'image_src', 'tag']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'logo_src']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'address', 'phone_number', 'opening_hours', 'image_src']

class HeaderConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderConfig
        fields = ['left_header_items', 'right_header_items', 'custom_css']

class FooterConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterConfig
        fields = ['links_visible', 'app_download_visible', 'newsletter_visible', 'custom_css']

class MainPageConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageConfig
        fields = ['highlights_visible', 'menu_visible', 'feature_visible', 'news_visible', 'custom_css', 'css_variables']