# management/commands/populate_config.py

from openai import OpenAI
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError
from api.models import Restaurant, HeaderConfig, FooterConfig, MainPageConfig
import json
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# example to generate app python manage.py populate_configs "A cozy bakery that specializes in artisan bread and pastries."

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_json_from_response(response: str) -> dict:
    # Find the start of the JSON block
    json_start = response.find('{')
    # Find the end of the JSON block
    json_end = response.rfind('}')
    
    # Extract the JSON string
    json_str = response[json_start:json_end+1]

    try:
        # Parse the JSON string into a Python dictionary
        json_data = json.loads(json_str)
        return json_data
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return {}
    
def generate_restaurant_data(description):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a creative restaurant name and three hex color codes for a restaurant that {description}. Please provide the name and colors in a JSON format with 'name', '--primary-color', '--secondary-color', and '--base-color'."},
    ]
    response = client.chat.completions.create(model="gpt-4o-mini",  messages=messages, stop=None, temperature=0.7)

    response_text = response.choices[0].message.content
    result = extract_json_from_response(response_text)
    return result

class Command(BaseCommand):
    help = 'Populate example configuration data for widgets'

    def add_arguments(self, parser):
        parser.add_argument('description', type=str, help='A description of what the restaurant does.')
        parser.add_argument('--username', type=str, default='testuser', help='Username for the sample user.')
        parser.add_argument('--email', type=str, default='test@example.com', help='Email for the sample user.')
        parser.add_argument('--password', type=str, default='password', help='Password for the sample user.')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']
        description = kwargs['description']

        # Generate restaurant data using OpenAI
        restaurant_data = generate_restaurant_data(description)

        restaurant_name = restaurant_data.get('name', 'Default Restaurant Name')
        primary_color = restaurant_data.get('--primary-color', '#d8e5d6')
        secondary_color = restaurant_data.get('--secondary-color', '#e6ff55')
        base_color = restaurant_data.get('--base-color', '#f4f3e7')

        # Create a sample user
        try:
            user = User.objects.create_user(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'User "{username}" created successfully.'))
        except IntegrityError:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists, skipping creation.'))

        # Create a sample restaurant
        try:
            restaurant = Restaurant.objects.create(name=restaurant_name)
            restaurant.users.add(user)
            self.stdout.write(self.style.SUCCESS(f'Restaurant "{restaurant_name}" created successfully.'))
        except IntegrityError:
            restaurant = Restaurant.objects.get(name=restaurant_name)
            self.stdout.write(self.style.WARNING(f'Restaurant "{restaurant_name}" already exists, skipping creation.'))

        # Create HeaderConfig
        try:
            HeaderConfig.objects.create(
                restaurant=restaurant,
                left_header_items=['Locations', 'Our Menu', 'The Market'],
                right_header_items=['Login', 'Cart', 'Our Mission'],
                custom_css=".header-container { }"
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
                custom_css=".footer-container { }"
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
                custom_css=".news-widget-container {  } \
                            .news-link-container {  } \
                            .picture-widget-container {  } \
                            .feature-widget-container {  } \
                            .highlights-widget-container {  } \
                            .menu-widget-container {  }",
                css_variables={
                    "--primary-color": primary_color,
                    "--secondary-color": secondary_color,
                    "--base-color": base_color,
                    "--font-size-base": "16px"
                }
            )
            self.stdout.write(self.style.SUCCESS('MainPageConfig created successfully.'))
        except IntegrityError:
            self.stdout.write(self.style.WARNING('MainPageConfig for the restaurant already exists, skipping creation.'))

        self.stdout.write(self.style.SUCCESS('Successfully populated example configuration data for the restaurant.'))

