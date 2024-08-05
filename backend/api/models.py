from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image_src = models.TextField()
    description = models.TextField()
    classification = models.CharField(max_length=100)

    def __str__(self):
        return self.name