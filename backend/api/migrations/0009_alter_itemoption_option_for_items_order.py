# Generated by Django 5.0.7 on 2024-09-16 19:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_itemoption_itemoption_unique_itemoption'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemoption',
            name='option_for_items',
            field=models.ManyToManyField(related_name='options', to='api.menuitem'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_type', models.CharField(choices=[('delivery', 'Delivery'), ('pickup', 'Pickup')], max_length=10)),
                ('store_location', models.CharField(max_length=255)),
                ('user_address', models.CharField(blank=True, max_length=255, null=True)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.restaurant')),
                ('selected_items', models.ManyToManyField(to='api.itemoption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
