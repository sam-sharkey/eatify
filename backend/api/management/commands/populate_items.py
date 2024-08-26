from django.core.management.base import BaseCommand
from django.db import IntegrityError
from api.models import MenuItem, Highlight, Restaurant

class Command(BaseCommand):
    help = 'Populate MenuItems and Highlights with predefined data'

    def handle(self, *args, **options):
        self.populate_menu_items()
        self.populate_highlights()

    def populate_menu_items(self):
        restaurant = Restaurant.objects.first()
        if not restaurant:
            self.stdout.write(self.style.ERROR("No restaurant found. Please add a restaurant first."))
            return

        menu_items = [
            {
                'name': 'Kale Caesar',
                'description': 'Chopped romaine, shredded kale, tomatoes, parmesan crisps, roasted chicken, shaved parmesan, caesar, lime squeeze',
                'price': 13.45,
                'calories': 510,
                'image_src': 'menu_items/KaleCaesar.png',
                'allergens': 'Dairy, Eggs',
                'tag': 'High Protein',
                'classification': 'Salads',
            },
            {
                'name': 'Guacamole Greens',
                'description': 'Chopped romaine, spring mix, shredded cabbage, tomatoes, tortilla chips, pickled onions, avocado, roasted chicken, lime squeeze, lime cilantro jalapeno vinaigrette',
                'price': 14.25,
                'calories': 575,
                'image_src': 'menu_items/GuacamoleGreens.png',
                'allergens': 'None',
                'tag': '',
                'classification': 'Salads',
            },
            {
                'name': 'Hummus Crunch',
                'description': 'Chopped romaine, shredded kale, basil, cucumbers, shredded cabbage, tomatoes, za\'atar breadcrumbs, chickpeas, pickled onions, hummus, pesto vinaigrette',
                'price': 13.25,
                'calories': 405,
                'image_src': 'menu_items/HummusCrunch.png',
                'allergens': 'Gluten',
                'tag': '',
                'classification': 'Salads',
            },
            {
                'name': 'Buffalo Chicken',
                'description': 'Chopped romaine, shredded kale, cilantro, tomatoes, za\'atar breadcrumbs, raw carrots, pickled onions, blue cheese, blackened chicken, caesar, sweetgreen hot sauce',
                'price': 14.95,
                'calories': 555,
                'image_src': 'menu_items/BuffaloChicken.png',
                'allergens': 'Dairy',
                'tag': 'High Protein',
                'classification': 'Salads',
            },
            {
                'name': 'Super Green Goddess',
                'description': 'Shredded kale, baby spinach, roasted sweet potatoes, shredded cabbage, spicy broccoli, roasted almonds, chickpeas, raw carrots, green goddess ranch',
                'price': 10.75,
                'calories': 455,
                'image_src': 'menu_items/SuperGreenGoddess.png',
                'allergens': 'Tree Nuts',
                'tag': 'Online Only',
                'classification': 'Salads',
            },
            {
                'name': 'Garden Cobb',
                'description': 'Chopped romaine, spring mix, roasted sweet potatoes, roasted almonds, tomatoes, avocado, hard boiled egg, blue cheese, balsamic vinaigrette',
                'price': 14.45,
                'calories': 745,
                'image_src': 'menu_items/GardenCobb.png',
                'allergens': 'Eggs, Dairy, Tree Nuts',
                'tag': 'Online Only',
                'classification': 'Salads',
            },
            {
                'name': 'BBQ Chicken Salad',
                'description': 'Chopped romaine, shredded kale, shredded cabbage, tomatoes, tortilla chips, apples, pickled onions, blackened chicken, green goddess ranch, honey bbq sauce',
                'price': 13.95,
                'calories': 520,
                'image_src': 'menu_items/BBQChickenSalad.png',
                'allergens': 'None',
                'tag': '',
                'classification': 'Salads',
            }
        ]
        menu_items += [
            {
                'name': 'Rosemary Focaccia',
                'image_src': 'menu_items/RosemaryFocaccia.png',
                'description': 'Locally-made rosemary focaccia, Check out our regional bakery partners here!',
                'classification': 'Sides',
            },
            {
                'name': 'Roasted Sweet Potatoes',
                'image_src': 'menu_items/RoastedSweetPotatoes.png',
                'description': 'Warm roasted sweet potatoes served with a choice of hot honey mustard or green goddess ranch',
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
        ]

        for item in menu_items:
            try:
                MenuItem.objects.create(restaurant=restaurant, **item)
                self.stdout.write(self.style.SUCCESS(f"MenuItem '{item['name']}' created successfully."))
            except IntegrityError:
                self.stdout.write(self.style.WARNING(f"MenuItem '{item['name']}' already exists."))

    def populate_highlights(self):
        restaurant = Restaurant.objects.first()
        if not restaurant:
            self.stdout.write(self.style.ERROR("No restaurant found. Please add a restaurant first."))
            return

        highlight_data = [
            {
                'title': 'SWEETGREEN EXCLUSIVES',
                'header': 'Dive into the fan favorites',
                'description1': 'Ordered often and always a hit, these popular picks are true sweetgreen staples.',
                'description2': 'This collection includes the Harvest Bowl, Kale Caesar, Guacamole Greens, Chicken Pesto Parm, and Hot Honey Chicken plate.',
                'image_src': 'highlights/SweetGreenExclusives.png',
                'tag': 'FeaturedMenu'
            },
            {
                'title': 'SWEETGREEN EXCLUSIVES',
                'header': 'Fuel up with high-protein picks',
                'description1': 'Let our top protein-rich options power your day',
                'description2': 'This hearty collection features our Harvest Bowl, Buffalo Chicken Bowl, Chicken Pesto Parm, and Hot Honey Chicken plate.',
                'image_src': 'highlights/ChickenSweetPotato.png',
                'tag': 'FeaturedMenu'
            },
            {
                'header': 'Introducing Caramelized Garlic Steak at Sweetgreen',
                'title': 'Grass-fed, pasture-raised',
                'image_src': 'highlights/SteakBowl.png',
                'tag': 'Highlight'
            },
            {
                'header': 'New Caramelized Garlic Steak',
                'title': 'Locally sourced ingredients',
                'image_src': 'highlights/Steak.png',
                'tag': 'Highlight'
            },
            {
                'header': 'Our Free Loyalty Program',
                'title': 'Download App Now',
                'image_src': 'highlights/LoyaltyApp.png',
                'tag': 'Highlight'
            },
            {
                'title': 'Good Morning America',
                'header': 'Naomi Osaka joins sweetgreen as youngest investor',
                'description1': 'Discover what our collab means for the future of fast food…',
                'image_src': 'highlights/GMA.png',
                'tag': 'News',
            },
            {
                'title': 'NEW YORK TIMES',
                'header': 'In a burger world, can sweetgreen scale up?',
                'description1': 'Learn how we\'re using tech to innovate fast-casual dining…',
                'image_src': 'highlights/NYT.png',
                'tag': 'News',
            },
            {
                'title': 'NPR HOW I BUILT THIS',
                'header': 'sweetgreen: Nicolas Jammet & Jonathan Neman',
                'description1': 'Dive into a juicy podcast with our visionary founders…',
                'image_src': 'highlights/NPR.png',
                'tag': 'News',
            }
        ]

        for highlight in highlight_data:
            try:
                Highlight.objects.create(restaurant=restaurant, **highlight)
                self.stdout.write(self.style.SUCCESS(f"Highlight '{highlight['title']}' created successfully."))
            except IntegrityError:
                self.stdout.write(self.style.WARNING(f"Highlight '{highlight['title']}' already exists."))

        self.stdout.write(self.style.SUCCESS("Highlights populated successfully!"))
