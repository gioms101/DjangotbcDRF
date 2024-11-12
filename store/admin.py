from django.contrib import admin
from .models import Product, Category, ProductTag


# Register your models here.

admin.site.register(ProductTag)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'image')
    list_filter = ('price', 'quantity')
    search_fields = ('name',)
    list_editable = ("quantity",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    list_select_related = ('parent',)
    search_fields = ('name',)
