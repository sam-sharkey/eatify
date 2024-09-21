from django.core.management.base import BaseCommand
from django.db import IntegrityError
from api.models import ItemOption, Location, Inventory
import random

class Command(BaseCommand):
    help = 'Populate MenuItems and Highlights with predefined data'

    def handle(self, *args, **options):
        restaurant_id=1
         # Get all ItemOptions for the restaurant
        item_options = ItemOption.objects.filter(restaurant_id=restaurant_id)
        
        # Get all Locations for the restaurant
        locations = Location.objects.filter(restaurant_id=restaurant_id)
        
        # Iterate over each ItemOption
        for item_option in item_options:
            # Iterate over each Location
            for location in locations:
                # Create an Inventory entry with a random quantity between 50 and 100
                quantity = random.randint(50, 100)
                
                # Create the Inventory item
                Inventory.objects.create(
                    item_option=item_option,
                    location=location,
                    quantity=quantity,
                    low_quantity_threshold=20  # Low quantity alert threshold set to 20
                )
                print(f"Created Inventory for ItemOption '{item_option.name}' at Location '{location.name}' with quantity {quantity}.")

