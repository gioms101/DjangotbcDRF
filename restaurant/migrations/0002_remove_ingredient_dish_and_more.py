# Generated by Django 5.0.7 on 2024-11-13 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='submenucategory',
            name='main_category',
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='MainMenuCategory',
        ),
        migrations.DeleteModel(
            name='SubMenuCategory',
        ),
    ]
