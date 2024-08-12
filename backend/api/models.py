from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='restaurants')

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

## ITEMS ON UI

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menuitems')
    name = models.CharField(max_length=100)
    image_src = models.ImageField(upload_to='menu_items/')
    description = models.TextField()
    classification = models.CharField(max_length=100)

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

class Highlight(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='highlights')
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    image_src = models.ImageField(upload_to='highlights/')
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
