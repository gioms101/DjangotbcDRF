# Generated by Django 5.0.7 on 2024-11-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_delete_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]