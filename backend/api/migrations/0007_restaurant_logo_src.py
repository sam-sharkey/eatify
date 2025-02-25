# Generated by Django 5.0.7 on 2024-09-01 16:45

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_highlight_image_src_alter_menuitem_image_src_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='logo_src',
            field=models.ImageField(blank=True, upload_to=api.models.Restaurant.upload_photo_to),
        ),
    ]
