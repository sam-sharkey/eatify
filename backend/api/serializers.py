from rest_framework import serializers
from .models import MenuItem, Highlight

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'image_src', 'description', 'classification']

class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = ['title', 'header', 'description1', 'description2', 'image_src', 'tag']