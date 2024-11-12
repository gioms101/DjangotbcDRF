from django.db import models
from django.template.defaultfilters import slugify

from .managers import ProductManager


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(to='Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to='products/', default='default.png')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    tags = models.ManyToManyField(ProductTag, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    objects = ProductManager()



