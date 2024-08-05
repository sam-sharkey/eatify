from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)