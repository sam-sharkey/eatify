# Generated by Django 5.0.7 on 2024-08-11 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_restaurant_mainpageconfig_headerconfig_footerconfig_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='highlight',
            name='unique_highlight',
        ),
        migrations.RemoveConstraint(
            model_name='menuitem',
            name='unique_menuitem',
        ),
        migrations.AddField(
            model_name='highlight',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='highlights', to='api.restaurant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='menuitems', to='api.restaurant'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='highlight',
            constraint=models.UniqueConstraint(fields=('restaurant', 'title', 'header', 'tag'), name='unique_highlight'),
        ),
        migrations.AddConstraint(
            model_name='menuitem',
            constraint=models.UniqueConstraint(fields=('name', 'restaurant'), name='unique_menuitem'),
        ),
    ]
