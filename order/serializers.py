from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id')
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.IntegerField(source='product.price')

    class Meta:
        model = CartItem
        fields = ['product_id', "product_name", 'product_price', 'quantity']


class AddToCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product']

