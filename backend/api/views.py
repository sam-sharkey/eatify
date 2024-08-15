from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem, Highlight, HeaderConfig, FooterConfig, MainPageConfig, Restaurant
from .serializers import MenuItemSerializer, RestaurantSerializer, HighlightSerializer, HeaderConfigSerializer, FooterConfigSerializer, MainPageConfigSerializer


class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return Restaurant.objects.filter(name=name)
        return Restaurant.objects.all()

    
class MenuItemsView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        # Filter highlights by restaurant_id
        return MenuItem.objects.filter(restaurant_id=restaurant_id)
    

class HighlightListView(generics.ListAPIView):
    serializer_class = HighlightSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        # Filter highlights by restaurant_id
        return Highlight.objects.filter(restaurant_id=restaurant_id)


class HeaderConfigView(APIView):
    def get(self, request, restaurant_id):
        try:
            config = HeaderConfig.objects.get(restaurant_id=restaurant_id)
            serializer = HeaderConfigSerializer(config)
            return Response(serializer.data)
        except HeaderConfig.DoesNotExist:
            return Response({"error": "HeaderConfig not found for the given restaurant"}, status=404)

class FooterConfigView(APIView):
    def get(self, request, restaurant_id):
        try:
            config = FooterConfig.objects.get(restaurant_id=restaurant_id)
            serializer = FooterConfigSerializer(config)
            return Response(serializer.data)
        except FooterConfig.DoesNotExist:
            return Response({"error": "FooterConfig not found for the given restaurant"}, status=404)

class MainPageConfigView(APIView):
    def get(self, request, restaurant_id):
        try:
            config = MainPageConfig.objects.get(restaurant_id=restaurant_id)
            serializer = MainPageConfigSerializer(config)
            return Response(serializer.data)
        except MainPageConfig.DoesNotExist:
            return Response({"error": "MainPageConfig not found for the given restaurant"}, status=404)
