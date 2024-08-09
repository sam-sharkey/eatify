from django.db import models

class MenuItem(models.Model):
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
                ],
                name="unique_menuitem",
            )
        ]

class Highlight(models.Model):
    header_line = models.CharField(max_length=255)
    body = models.TextField()
    background_image = models.ImageField(upload_to='highlights/')

    def __str__(self):
        return self.header_line
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "header_line",
                ],
                name="unique_highlight",
            )
        ]
