from rest_framework import serializers
from .models import MenuItem, Highlight, Restaurant, HeaderConfig, Inventory, FooterConfig, MainPageConfig, Location, ItemOption, OrderItemOption, Order


class OrderItemOptionSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item_option.name')
    item_price = serializers.DecimalField(source='item_option.cost', max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItemOption
        fields = ['item_name', 'item_price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    item_options = OrderItemOptionSerializer(source='orderitemoption_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'delivery_type', 'store_location', 'user_address', 'total_cost', 'order_time', 'status', 'item_options']

    def update(self, instance, validated_data):
        # Handle updating selected items separately
        selected_items_data = validated_data.pop('item_options', None)

        # Update the main fields of the order
        instance.delivery_type = validated_data.get('delivery_type', instance.delivery_type)
        instance.store_location = validated_data.get('store_location', instance.store_location)
        instance.user_address = validated_data.get('user_address', instance.user_address)
        instance.total_cost = validated_data.get('total_cost', instance.total_cost)
        instance.order_time = validated_data.get('order_time', instance.order_time)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        # If there are selected items, update them
        if selected_items_data is not None:
            # Clear out existing items before re-adding them
            instance.orderitemoption_set.all().delete()

            # Add the new selected items
            for item_data in selected_items_data:
                item_option = item_data['item_option']
                quantity = item_data['quantity']
                OrderItemOption.objects.create(order=instance, item_option=item_option, quantity=quantity)

        return instance

class InventorySerializer(serializers.ModelSerializer):
    item_option_name = serializers.CharField(source='item_option.name', read_only=True)
    location_name = serializers.CharField(source='location.name', read_only=True)
    is_low_stock = serializers.SerializerMethodField()

    class Meta:
        model = Inventory
        fields = ['id', 'item_option', 'location', 'quantity', 'low_quantity_threshold', 'is_low_stock', 'item_option_name', 'location_name']
        read_only_fields = ['item_option', 'location', 'is_low_stock']

    def get_is_low_stock(self, obj):
        return obj.is_low_stock()


class ItemOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOption
        fields = ['id', 'image_src', 'name', 'calories', 'cost', 'classification', 'is_in_stock']

class MenuItemSerializer(serializers.ModelSerializer):
    options = ItemOptionSerializer(many=True, read_only=True)
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'classification', 'price', 'calories', 'image_src', 'allergens', 'tag', 'options']

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