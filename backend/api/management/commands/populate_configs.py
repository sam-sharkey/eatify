# management/commands/populate_config.py

from openai import OpenAI
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError
from api.models import Restaurant, HeaderConfig, FooterConfig, MainPageConfig, Location
import json
from dotenv import load_dotenv
import os
import requests

load_dotenv()  # Load environment variables from .env file

# example to generate app python manage.py populate_configs "A cozy bakery that specializes in artisan bread and pastries."

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

def extract_json_from_response(response: str) -> dict:
    try:
        # Try to directly load the response assuming it's valid JSON
        return json.loads(response)
    except json.JSONDecodeError as e:
        print(f"Initial JSON decode failed: {e}. Attempting to fix the JSON format.")

        # If it fails, attempt to manually wrap the JSON objects in a list
        try:
            json_start = response.find('{')
            json_end = response.rfind('}')
            
            # Extract the JSON string
            json_str = response[json_start:json_end+1]

            # Split by '},' to find individual objects
            json_objects = json_str.split('},')

            # Reattach missing closing braces and wrap in a list
            json_objects = [obj.strip() + ('}' if not obj.endswith('}') else '') for obj in json_objects]
            json_str_fixed = '[' + ','.join(json_objects) + ']'

            # Attempt to load the fixed JSON string
            return json.loads(json_str_fixed)
        except Exception as ex:
            print(f"Failed to fix and decode JSON: {ex}")
            return {}
    
def generate_restaurant_data(description):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a creative restaurant name and three hex color codes for a "
         f"restaurant that {description}. The colors should go with the theme of the restaurant and look good together. "
         f"Please provide the name and colors in a JSON format with 'name', '--primary-color', '--secondary-color', and '--base-color'."},
    ]
    response = client.chat.completions.create(model="gpt-4o-mini",  messages=messages, stop=None, temperature=0.7)

    response_text = response.choices[0].message.content
    result = extract_json_from_response(response_text)
    return result


def generate_location_data(restaurant_name: str, num_locations: int = 5) -> list:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate {num_locations} locations for a restaurant called "
         f"'{restaurant_name}'. For each location, provide the name, address, phone number, opening hours, "
         f"and an image description for what the outside of the restaurant looks like. "
         f"Please return the information in a JSON format with fields: 'name', 'address', 'phone_number', 'opening_hours', and 'image_description'."}
    ]
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages, stop=None, temperature=0.7)
    response_text = response.choices[0].message.content
    location_data = extract_json_from_response(response_text)
    if isinstance(location_data, list):
        return location_data
    else:
        return []

def generate_locations_for_restaurant(restaurant, num_locations=3):
    locations_data = generate_location_data(restaurant.name, num_locations)

    for loc_data in locations_data:
        image_src = None
        if 'image_description' in loc_data and loc_data['image_description']:
            image_url = generate_image(loc_data['image_description'])
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_filename = f"{loc_data['name'].replace(' ', '_')}.png"
                try:
                    os.mkdir(f"media/{restaurant.name}/locations/")
                except OSError as error:
                    pass
                image_path = f"{restaurant.name}/locations/{image_filename}"
                with open(f"media/{image_path}", 'wb') as img_file:
                    img_file.write(image_response.content)
                image_src = image_path

        Location.objects.create(
            restaurant=restaurant,
            name=loc_data["name"],
            address=loc_data["address"],
            phone_number=loc_data["phone_number"],
            opening_hours=loc_data["opening_hours"],
            image_src=image_src or "default_location.png",
        )


def generate_image(description):
        response = client.images.generate(
            model="dall-e-2",
            prompt=description,
            n=1,
            size="1024x1024",
            quality="standard",
        )

        return response.data[0].url  # This returns the URL of the generated image

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
            # Generate an image using DALL-E or a similar model
            image_url = generate_image(f"Generate a simple logo for a restaurant called {restaurant_name}. It should have a clear background.")

            # Download the image
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_filename = f"{restaurant_name.replace(' ', '_')}.png"
                try:
                    os.mkdir(f"media/{restaurant_name}")
                except OSError as error:
                    pass
                image_path = f"{restaurant_name}/{image_filename}"

                with open(f"media/{image_path}", 'wb') as img_file:
                    img_file.write(image_response.content)

            restaurant = Restaurant.objects.create(name=restaurant_name, logo_src=image_path)
            restaurant.users.add(user)
            self.stdout.write(self.style.SUCCESS(f'Restaurant "{restaurant_name}" created successfully.'))

            # Generate locations for the restaurant
            restaurant = Restaurant.objects.last()
            generate_locations_for_restaurant(restaurant, num_locations=5)
            self.stdout.write(self.style.SUCCESS(f'Locations for "{restaurant_name}" created successfully.'))
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

