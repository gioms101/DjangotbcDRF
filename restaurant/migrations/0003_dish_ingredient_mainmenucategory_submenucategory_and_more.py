# Generated by Django 5.0.7 on 2024-11-13 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_ingredient_dish_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='restaurant.dish')),
            ],
        ),
        migrations.CreateModel(
            name='MainMenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_categories', to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='SubMenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='restaurant.mainmenucategory')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='restaurant.submenucategory'),
        ),
    ]
