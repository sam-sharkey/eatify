from rest_framework import serializers
from .models import MenuItem, Highlight

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'image_src', 'description', 'classification']


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = ['id', 'header_line', 'body', 'background_image']
