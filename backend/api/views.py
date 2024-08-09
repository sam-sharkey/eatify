from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem, Highlight
from .serializers import MenuItemSerializer, HighlightSerializer

class MenuItemsView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
    

class HighlightListView(generics.ListAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer