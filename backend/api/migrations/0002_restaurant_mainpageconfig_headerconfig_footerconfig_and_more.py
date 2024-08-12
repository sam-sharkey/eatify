# Generated by Django 5.0.7 on 2024-08-11 20:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('users', models.ManyToManyField(related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainPageConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlights_visible', models.BooleanField(default=True)),
                ('menu_visible', models.BooleanField(default=True)),
                ('feature_visible', models.BooleanField(default=True)),
                ('news_visible', models.BooleanField(default=True)),
                ('custom_css', models.TextField(blank=True, null=True)),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='main_page_config', to='api.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='HeaderConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_header_items', models.JSONField(default=list)),
                ('right_header_items', models.JSONField(default=list)),
                ('custom_css', models.TextField(blank=True, null=True)),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='header_config', to='api.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='FooterConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links_visible', models.BooleanField(default=True)),
                ('app_download_visible', models.BooleanField(default=True)),
                ('newsletter_visible', models.BooleanField(default=True)),
                ('custom_css', models.TextField(blank=True, null=True)),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='footer_config', to='api.restaurant')),
            ],
        ),
        migrations.AddConstraint(
            model_name='restaurant',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_restaurant'),
        ),
        migrations.AddConstraint(
            model_name='mainpageconfig',
            constraint=models.UniqueConstraint(fields=('restaurant',), name='unique_mainpage'),
        ),
        migrations.AddConstraint(
            model_name='headerconfig',
            constraint=models.UniqueConstraint(fields=('restaurant',), name='unique_header'),
        ),
        migrations.AddConstraint(
            model_name='footerconfig',
            constraint=models.UniqueConstraint(fields=('restaurant',), name='unique_footer'),
        ),
    ]
