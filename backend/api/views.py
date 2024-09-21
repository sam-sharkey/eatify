from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem, Highlight, HeaderConfig, FooterConfig, MainPageConfig, Restaurant, Location, ItemOption, Order, OrderItemOption
from .serializers import MenuItemSerializer, OrderSerializer, RestaurantSerializer, HighlightSerializer, HeaderConfigSerializer, FooterConfigSerializer, MainPageConfigSerializer, LocationSerializer, ItemOptionSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return Restaurant.objects.filter(name=name)
        return Restaurant.objects.all()

class LocationView(generics.ListAPIView):
    def get(self, request, restaurant_id):
        try:
            locations = Location.objects.filter(restaurant_id=restaurant_id)
            serializer = LocationSerializer(locations, many=True)
            return Response(serializer.data)
        except Location.DoesNotExist:
            return Response({"error": "Locations not found for the given restaurant"}, status=404)
    
class MenuItemsView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        # Filter highlights by restaurant_id
        return MenuItem.objects.filter(restaurant_id=restaurant_id)
    
class ItemOptionView(generics.ListAPIView):
    serializer_class = ItemOptionSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        # Filter ItemOption by restaurant_id
        return ItemOption.objects.filter(restaurant_id=restaurant_id)

class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'  # To identify orders by their ID in the URL

    def get(self, request):
        """
        Overrides the default GET method to support filtering by order_id or restaurant_id.
        """
        try:
            if 'restaurant_id' in request.query_params.keys():
                orders = Order.objects.filter(restaurant_id=request.query_params['restaurant_id'])
            elif 'order_id' in request.query_params.keys():
                orders = Order.objects.filter(id=request.query_params['order_id'])
            else:
                orders = Order.objects.all()
            
            # Serialize the orders
            order_serializer = OrderSerializer(orders, many=True)
            return Response(order_serializer.data, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, restaurant_id):
        """
        Create a new order.
        """
        try:
            data = request.data
            #user = request.user

            # Create the Order
            order = Order.objects.create(
                restaurant=Restaurant.objects.get(id=restaurant_id),
                #user=user,
                delivery_type=data['deliveryType'],
                #store_location=Location.objects.get(name=data['storeLocation']),
                user_address=data['userAddress'],
                total_cost=data['totalCost'],
            )

            # Add selected items to the Order
            for item_data in data['selectedItems']:
                item = ItemOption.objects.get(id=item_data['item_option']['id'])
                OrderItemOption.objects.create(order=order, item_option=item, quantity=item_data['quantity'])

            total_cost = sum(item.total_item_price() for item in order.orderitemoption_set.all())
            order.total_cost = total_cost
            order.save()
            return Response({"message": order.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Handle PUT requests to update an existing order.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()  # Get the order instance using lookup_field (id)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        # Validate data
        serializer.is_valid(raise_exception=True)

        # Perform update
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        """
        Override this method if you need to add additional save logic.
        """
        # Example of additional update logic
        order = serializer.save()

        # Recalculate total cost if necessary
        total_cost = sum(item.total_item_price() for item in order.orderitemoption_set.all())
        order.total_cost = total_cost
        order.save()

    def destroy(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete an existing order.
        """
        instance = self.get_object()  # Get the order instance using lookup_field (id)
        self.perform_destroy(instance)
        return Response({"message": "Order deleted"}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        """
        Custom method to handle the deletion of an order.
        """
        instance.delete()

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
