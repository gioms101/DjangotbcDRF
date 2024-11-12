from django.db import models
from user.models import CustomUser
from store.models import Product
from .managers import CartItemManager


# Create your models here.

class UserCard(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(UserCard, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Item of {self.cart}'

    objects = CartItemManager()
