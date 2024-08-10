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
                    "title",
                    "header",
                    "tag"
                ],
                name="unique_highlight",
            )
        ]