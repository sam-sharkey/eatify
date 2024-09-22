from django.db import models
from django.contrib.auth.models import User


# Restaurant Info

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='restaurants')
    def upload_photo_to(self, filename):
        return f'{self.name}/{filename}'
    
    logo_src = models.ImageField(upload_to=upload_photo_to, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                ],
                name="unique_restaurant",
            )
        ]

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='locations')

    def upload_photo_to(self, filename):
        return f'{self.restaurant.name}/locations/{filename}'
    
    image_src = models.ImageField(upload_to=upload_photo_to)

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                    "restaurant",
                ],
                name="unique_locations",
            )
        ]

## ITEMS ON UI

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menuitems')
    name = models.CharField(max_length=100)

    def upload_photo_to(self, filename):
        return f'{self.restaurant.name}/menu_items/{filename}'
    
    image_src = models.ImageField(upload_to=upload_photo_to)
    description = models.TextField()
    classification = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.IntegerField()
    allergens = models.CharField(max_length=255, blank=True)
    tag = models.CharField(max_length=50, blank=True)  # e.g., "Online Only", "High Protein"

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                    "restaurant",
                ],
                name="unique_menuitem",
            )
        ]

class ItemOption(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='itemoptions')
    name = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    classification = models.CharField(max_length=50)  # e.g. "Base", "Premium", "Dressing", "Sweetener"
    is_in_stock = models.BooleanField(default=True)
    option_for_items = models.ManyToManyField(MenuItem, related_name='options')
    def upload_photo_to(self, filename):
        return f'{self.restaurant.name}/option/{filename}'
    
    image_src = models.ImageField(upload_to=upload_photo_to, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                    "restaurant",
                ],
                name="unique_itemoption",
            )
        ]

# Inventory

class Inventory(models.Model):
    item_option = models.ForeignKey(ItemOption, on_delete=models.CASCADE, related_name='inventories')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='inventories')
    quantity = models.PositiveIntegerField(default=0)  # Inventory quantity available
    low_quantity_threshold = models.PositiveIntegerField(default=0)  # Threshold for low stock alerts

    def __str__(self):
        return f'{self.item_option.name} at {self.location.name}: {self.quantity}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['item_option', 'location'],
                name='unique_itemoption_location'
            )
        ]

    # Custom method to check if the stock is below the low quantity threshold
    def is_low_stock(self):
        return self.quantity <= self.low_quantity_threshold



# Order Management

class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    DELIVERY_CHOICES = [
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup'),
    ]
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_CHOICES)
    store_location = models.CharField(max_length=255, null=True)
    user_address = models.CharField(max_length=255, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="not_started")

    def __str__(self):
        return f"Order {self.id} by person"#{self.user.username}"
    
    # Relationship to ItemOption via OrderItemOption
    item_options = models.ManyToManyField(ItemOption, through='OrderItemOption')

class OrderItemOption(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_option = models.ForeignKey(ItemOption, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # Quantity for each item in the order

    def total_item_price(self):
        return self.item_option.cost * self.quantity

# Staff

class Staff(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='staff')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    timings = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.position})"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email'],
                name='unique_email'
            )
        ]


# News Related

class Highlight(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='highlights')
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)

    def upload_photo_to(self, filename):
        return f'{self.restaurant.name}/highlights/{filename}'
    image_src = models.ImageField(upload_to=upload_photo_to)

    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "restaurant",
                    "title",
                    "header",
                    "tag"
                ],
                name="unique_highlight",
            )
        ]

## MODELS FOR WIDGETS

class HeaderConfig(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name='header_config')
    left_header_items = models.JSONField(default=list)
    right_header_items = models.JSONField(default=list)
    custom_css = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"HeaderConfig for {self.restaurant}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "restaurant",
                ],
                name="unique_header",
            )
        ]

class FooterConfig(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name='footer_config')
    links_visible = models.BooleanField(default=True)
    app_download_visible = models.BooleanField(default=True)
    newsletter_visible = models.BooleanField(default=True)
    custom_css = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"FooterConfig for {self.restaurant}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "restaurant",
                ],
                name="unique_footer",
            )
        ]

class MainPageConfig(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name='main_page_config')
    highlights_visible = models.BooleanField(default=True)
    menu_visible = models.BooleanField(default=True)
    feature_visible = models.BooleanField(default=True)
    news_visible = models.BooleanField(default=True)
    custom_css = models.TextField(blank=True, null=True)
    css_variables = models.JSONField(default=dict)  # Add this field to store CSS variables

    def __str__(self):
        return f"MainPageConfig for {self.restaurant}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "restaurant",
                ],
                name="unique_mainpage",
            )
        ]
