from django.db import models
from user.models import CustomUser

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)
    photo = models.ImageField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MainMenuCategory(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='main_categories')

    def __str__(self):
        return self.name


class SubMenuCategory(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(blank=True, null=True)
    main_category = models.ForeignKey(MainMenuCategory, on_delete=models.CASCADE, related_name='sub_categories')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    sub_category = models.ForeignKey(SubMenuCategory, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name
