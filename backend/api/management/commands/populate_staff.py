from django.core.management.base import BaseCommand
from api.models import Restaurant, Staff
import random

class Command(BaseCommand):
    help = 'Populate the Ingredient model with hardcoded data'

    def handle(self, *args, **kwargs):
        restaurant = Restaurant.objects.first()
        positions = ['Manager', 'Chef', 'Waiter', 'Cleaner', 'Cashier']
        names = [
            'John Doe', 'Jane Smith', 'Tom Hanks', 'Emma Watson',
            'Chris Evans', 'Scarlett Johansson', 'Robert Downey',
            'Natalie Portman', 'Mark Ruffalo', 'Samuel Jackson'
        ]

        for i, name in enumerate(names):
            Staff.objects.create(
                restaurant=restaurant,
                staff_id=f'#10{i+1}',
                name=name,
                position=random.choice(positions),
                email=f'{name.lower().replace(" ", ".")}@eatify.com',
                phone=f'+1 (555) 555-100{i}',
                age=random.randint(25, 50),
                salary=round(random.uniform(2000, 5000), 2),
                timings='9am to 6pm'
            )

        print("Successfully populated 10 staff members!")
