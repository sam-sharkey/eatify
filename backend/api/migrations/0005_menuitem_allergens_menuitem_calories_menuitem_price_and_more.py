# Generated by Django 5.0.7 on 2024-08-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_mainpageconfig_css_variables'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='allergens',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='calories',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='tag',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
