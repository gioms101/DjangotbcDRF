# Generated by Django 5.0.7 on 2024-11-13 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_restaurant_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenucategory',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_categories', to='restaurant.restaurant'),
        ),
    ]
