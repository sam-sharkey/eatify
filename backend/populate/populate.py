import django
from django.db import IntegrityError

# DJANGO
django.setup()

from api.models import Highlight, MenuItem

highlights = [
    {
        'header_line': 'Introducing Caramelized Garlic Steak at Sweetgreen',
        'body': 'Grass-fed, pasture-raised',
        'background_image': 'highlights/SteakBowl.png',
    },
    {
        'header_line': 'New Caramelized Garlic Steak',
        'body': 'Locally sourced ingredients',
        'background_image': 'highlights/Steak.png',
    },
    {
        'header_line': 'Our Free Loyalty Program',
        'body': 'Download App Now',
        'background_image': 'highlights/LoyaltyApp.png',
    },
]

for highlight in highlights:
    try:
        Highlight.objects.create(**highlight)
    except IntegrityError:
        continue

print("Highlights populated successfully!")

# Populate MenuItems
menu_items = [
    {
        'name': 'Rosemary Focaccia',
        'image_src': 'menu_items/RosemaryFocaccia.png',
        'description': 'Locally-made rosemary focaccia, Check out our regional bakery partners here!',
        'classification': 'Sides',
    },
    {
        'name': 'Roasted Sweet Potatoes',
        'image_src': 'menu_items/RoastedSweetPotatoes.png',
        'description': 'Warm roasted sweet potatoes seved with a choice of hot honey mustard or green goddess ranch',
        'classification': 'Sides',
    },
    {
        'name': 'Hibiscus Clover Tea',
        'image_src': 'menu_items/HibiscusCloverTea.png',
        'description': 'Refreshing crimson clover tea mixed with bright berries and tangy hibiscus',
        'classification': 'Sides',
    },
    {
        'name': 'Harvest Bowl',
        'image_src': 'menu_items/HarvestBowl.png',
        'description': 'Roasted chicken, roasted sweet potatoes, apples, goat cheese, roasted almonds, wild rice, shredded kale, balsamic vinaigrette',
        'classification': 'Warm Bowls',
    },
    {
        'name': 'Chicken Pesto Parm',
        'image_src': 'menu_items/ChickenPestoParm.png',
        'description': 'Roasted chicken, spicy broccoli, tomatoes, shaved parmesan, za\'atar breadcrumbs, warm quinoa, baby spinach, sweetgreen hot sauce, pesto vinaigrette',
        'classification': 'Warm Bowls',
    },
    {
        'name': 'Shroomami',
        'image_src': 'menu_items/Shroomami.png',
        'description': 'Roasted tofu, warm portobello mix, cucumbers, basil, shredded cabbage, roasted almonds, wild rice, shredded kale, miso sesame ginger dressing',
        'classification': 'Warm Bowls',
    },
    {
        'name': 'Buffalo Chicken',
        'image_src': 'menu_items/BuffaloChicken.png',
        'description': 'Blackened chicken, pickled onions, tomatoes, raw carrots, cilantro, blue cheese, za’atar breadcrumbs, shredded kale, chopped romaine, sweetgreen hot sauce, caesar',
        'classification': 'Salads',
    },
    {
        'name': 'Guacamole Greens',
        'image_src': 'menu_items/GuacamoleGreens.png',
        'description': 'Roasted chicken, avocado, tomatoes, pickled onions, shredded cabbage, tortilla chips, spring mix, chopped romaine, lime squeeze, lime cilantro jalapeño vinaigrette',
        'classification': 'Salads',
    },
    {
        'name': 'Kale Caesar',
        'image_src': 'menu_items/KaleCaeser.png',
        'description': 'Roasted chicken, tomatoes, parmesan crisps, shaved parmesan, shredded kale, chopped romaine, lime squeeze, caesar',
        'classification': 'Salads',
    },
]

for item in menu_items:
    try:
        MenuItem.objects.create(**item)
    except IntegrityError:
        continue
