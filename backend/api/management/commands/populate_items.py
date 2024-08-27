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
            # Featured
            {
                'name': 'Caramelized Garlic Steak',
                'description': 'Wild rice, spicy broccoli, tomatoes, warm roasted sweet potatoes, caramelized garlic steak, pesto vinaigrette',
                'price': 17.15,
                'calories': 860,
                'image_src': 'menu_items/caramelized_garlic_steak.png',
                'allergens': 'None',
                'tag': 'New!',
                'classification': 'Featured',
            },
            {
                'name': 'Steakhouse Chopped',
                'description': 'Chopped romaine, herbed quinoa, shredded cabbage, tomatoes, crispy onions, blue cheese, caramelized garlic steak, green goddess ranch',
                'price': 17.15,
                'calories': 815,
                'image_src': 'menu_items/steakhouse_chopped.png',
                'allergens': 'Dairy',
                'tag': 'New!',
                'classification': 'Featured',
            },
            {
                'name': 'Kale Caesar (Steak)',
                'description': 'Chopped romaine, shredded kale, tomatoes, parmesan crisps, shaved parmesan, caramelized garlic steak, caesar, lime squeeze',
                'price': 16.15,
                'calories': 720,
                'image_src': 'menu_items/kale_caesar_steak.png',
                'allergens': 'Dairy, Eggs',
                'tag': 'New!',
                'classification': 'Featured',
            },
            # New High Protein Items
            {
                'name': 'Hot Honey Chicken',
                'description': 'Herbed quinoa, crispy onions, blackened chicken, warm roasted sweet potatoes, veg slaw, hot honey mustard sauce',
                'price': 15.45,
                'calories': 835,
                'image_src': 'menu_items/hot_honey_chicken.png',
                'allergens': 'None',
                'tag': 'High Protein',
                'classification': 'High Protein',
            },
            {
                'name': 'Miso Glazed Salmon',
                'description': 'White rice, cucumbers, nori sesame seasoning, crispy onions, pickled onions, avocado, miso glazed salmon, spicy cashew',
                'price': 16.95,
                'calories': 930,
                'image_src': 'menu_items/miso_glazed_salmon.png',
                'allergens': 'Fish, Tree Nuts',
                'tag': 'High Protein',
                'classification': 'High Protein',
            },
            # New Bowls Items
            {
                'name': 'Harvest Bowl',
                'description': 'Shredded kale, wild rice, roasted sweet potatoes, roasted almonds, apples, goat cheese, roasted chicken, balsamic vinaigrette',
                'price': 14.45,
                'calories': 765,
                'image_src': 'menu_items/harvest_bowl.png',
                'allergens': 'Dairy, Tree Nuts',
                'tag': 'High Protein',
                'classification': 'Bowls',
            },
            {
                'name': 'Shroomami',
                'description': 'Shredded kale, wild rice, basil, cucumbers, shredded cabbage, roasted almonds, warm portobello mix, roasted tofu, miso sesame ginger',
                'price': 13.95,
                'calories': 685,
                'image_src': 'menu_items/shroomami.png',
                'allergens': 'Tree Nuts, Soy',
                'tag': '',
                'classification': 'Bowls',
            },
            {
                'name': 'Crispy Rice Bowl',
                'description': 'Arugula, wild rice, cilantro, cucumbers, shredded cabbage, roasted almonds, crispy rice, raw carrots, blackened chicken, lime squeeze, spicy cashew',
                'price': 14.95,
                'calories': 640,
                'image_src': 'menu_items/crispy_rice_bowl.png',
                'allergens': 'Tree Nuts',
                'tag': 'High Protein',
                'classification': 'Bowls',
            },
            {
                'name': 'Chicken Pesto Parm',
                'description': 'Baby spinach, herbed quinoa, spicy broccoli, tomatoes, za\'atar breadcrumbs, roasted chicken, shaved parmesan, pesto vinaigrette, sweetgreen hot sauce',
                'price': 14.45,
                'calories': 540,
                'image_src': 'menu_items/chicken_pesto_parm.png',
                'allergens': 'Dairy',
                'tag': 'High Protein',
                'classification': 'Bowls',
            },
            {
                'name': 'Chicken Avocado Ranch',
                'description': 'Chopped romaine, white rice, tortilla chips, apples, pickled onions, avocado, blackened chicken, green goddess ranch',
                'price': 14.25,
                'calories': 705,
                'image_src': 'menu_items/chicken_avocado_ranch.png',
                'allergens': 'Dairy',
                'tag': '',
                'classification': 'Bowls',
            },
            {
                'name': 'Fish Taco',
                'description': 'Arugula, herbed quinoa, cilantro, shredded cabbage, tortilla chips, avocado, miso glazed salmon, lime cilantro jalapeno vinaigrette, sweetgreen hot sauce',
                'price': 16.95,
                'calories': 835,
                'image_src': 'menu_items/fish_taco.png',
                'allergens': 'Fish, Tree Nuts',
                'tag': 'Online Only',
                'classification': 'Bowls',
            },
            # Sides
            {
                'name': 'Rosemary Focaccia',
                'description': 'Freshly baked daily. *Contains Common Allergens, Including Gluten. More Info At Sweetgreen.Com/Menu',
                'price': 2.35,
                'calories': 230,
                'image_src': 'menu_items/rosemary_focaccia.png',
                'allergens': 'Gluten',
                'tag': '',
                'classification': 'Sides',
            },
            {
                'name': 'Roasted Sweet Potatoes + Hot Honey Mustard',
                'description': 'Hot roasted sweet potatoes, hot honey sauce. *No Modifications (Yet!). Contains Common Allergens. More info at sweetgreen.com/menu',
                'price': 4.15,
                'calories': 340,
                'image_src': 'menu_items/roasted_sweet_potatoes_hot_honey.png',
                'allergens': '',
                'tag': '',
                'classification': 'Sides',
            },
            {
                'name': 'Hummus + Focaccia',
                'description': 'Freshly baked rosemary focaccia breadsticks with smooth hummus. *Contains common allergens, including gluten. More info at sweetgreen.com/menu',
                'price': 4.15,
                'calories': 290,
                'image_src': 'menu_items/hummus_focaccia.png',
                'allergens': 'Gluten',
                'tag': '',
                'classification': 'Sides',
            },
            {
                'name': 'Roasted Sweet Potatoes + Green Goddess Ranch',
                'description': 'Hot roasted sweet potatoes, green goddess ranch. *No Modifications (Yet!). Contains Common Allergens, Including Dairy And Eggs. More Info At Sweetgreen.Com/Menu',
                'price': 4.15,
                'calories': 340,
                'image_src': 'menu_items/roasted_sweet_potatoes_green_goddess.png',
                'allergens': 'Dairy, Eggs',
                'tag': '',
                'classification': 'Sides',
            },
            {
                'name': 'SG X Siete: Green Goddess Ranch Potato Chips',
                'description': 'Kettle-cooked and inspired by our Green Goddess Ranch dressing flavor, made with avocado oil and a hint of poblano. Only available at sweetgreen.',
                'price': 2.85,
                'calories': 220,
                'image_src': 'menu_items/sg_siete_green_goddess_chips.png',
                'allergens': '',
                'tag': '',
                'classification': 'Sides',
            },
            {
                'name': 'Siete Sea Salt Potato Chips',
                'description': 'Kettle-cooked and made with sea salt and avocado oil for a light, salty crunch.',
                'price': 2.85,
                'calories': 210,
                'image_src': 'menu_items/siete_sea_salt_chips.png',
                'allergens': '',
                'tag': '',
                'classification': 'Sides',
            },

            # New Desserts Items
            {
                'name': 'Crispy Rice Treat',
                'description': 'Crispy organic brown rice, quinoa, and puffed millet—naturally sweetened with honey date caramel and just 6g of sugar. *This product is gluten-free but contains common allergens, including dairy and tree nuts. More info at sweetgreen.com/menu',
                'price': 3.15,
                'calories': 190,
                'image_src': 'menu_items/crispy_rice_treat.png',
                'allergens': 'Dairy, Tree Nuts',
                'tag': '',
                'classification': 'Desserts',
            },
            {
                'name': 'Hu Cashews + Vanilla Bean Hunks',
                'description': 'Organic snackable dark chocolate covered cashews with a pinch of sea salt and no refined sugar. *This product is gluten-free and vegan but contains cashew & coconut. May contain dairy, peanuts & other tree nuts. More info at sweetgreen.com/menu.',
                'price': 3.15,
                'calories': 170,
                'image_src': 'menu_items/hu_cashews_vanilla_bean_hunks.png',
                'allergens': 'Cashew, Coconut',
                'tag': '',
                'classification': 'Desserts',
            },
            {
                'name': 'Hu Salty Dark Chocolate Bar',
                'description': 'Organic dark chocolate with a pinch of sea salt and no refined sugar. *This product is gluten-free and vegan but contains coconut. May contain other tree nuts & dairy. More info at sweetgreen.com/menu.',
                'price': 6.15,
                'calories': 380,
                'image_src': 'menu_items/hu_salty_dark_chocolate_bar.png',
                'allergens': 'Coconut',
                'tag': '',
                'classification': 'Desserts',
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
