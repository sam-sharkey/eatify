# management/commands/populate_config.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError
from api.models import Restaurant, HeaderConfig, FooterConfig, MainPageConfig

class Command(BaseCommand):
    help = 'Populate example configuration data for widgets'

    def handle(self, *args, **kwargs):
        # Create a sample user
        try:
            user = User.objects.create_user('testuser', 'test@example.com', 'password')
            self.stdout.write(self.style.SUCCESS('User "testuser" created successfully.'))
        except IntegrityError:
            user = User.objects.get(username='testuser')
            self.stdout.write(self.style.WARNING('User "testuser" already exists, skipping creation.'))

        # Create a sample restaurant
        try:
            restaurant = Restaurant.objects.create(name='Sample Restaurant')
            restaurant.users.add(user)
            self.stdout.write(self.style.SUCCESS('Restaurant "Sample Restaurant" created successfully.'))
        except IntegrityError:
            restaurant = Restaurant.objects.get(name='Sample Restaurant')
            self.stdout.write(self.style.WARNING('Restaurant "Sample Restaurant" already exists, skipping creation.'))

        # Create HeaderConfig
        try:
            HeaderConfig.objects.create(
                restaurant=restaurant,
                left_header_items=['Locations', 'Our Menu', 'The Market'],
                right_header_items=['Login', 'Cart'],
                custom_css="header { background-color: #f0f0f0; }"
            )
            self.stdout.write(self.style.SUCCESS('HeaderConfig created successfully.'))
        except IntegrityError:
            self.stdout.write(self.style.WARNING('HeaderConfig for the restaurant already exists, skipping creation.'))

        # Create FooterConfig
        try:
            FooterConfig.objects.create(
                restaurant=restaurant,
                links_visible=True,
                app_download_visible=True,
                newsletter_visible=True,
                custom_css="footer { color: #333; }"
            )
            self.stdout.write(self.style.SUCCESS('FooterConfig created successfully.'))
        except IntegrityError:
            self.stdout.write(self.style.WARNING('FooterConfig for the restaurant already exists, skipping creation.'))

        # Create MainPageConfig
        try:
            MainPageConfig.objects.create(
                restaurant=restaurant,
                highlights_visible=True,
                menu_visible=True,
                feature_visible=True,
                news_visible=True,
                custom_css="body { font-size: 14px; }"
            )
            self.stdout.write(self.style.SUCCESS('MainPageConfig created successfully.'))
        except IntegrityError:
            self.stdout.write(self.style.WARNING('MainPageConfig for the restaurant already exists, skipping creation.'))

        self.stdout.write(self.style.SUCCESS('Successfully attempted to populate example configuration data for restaurant.'))
