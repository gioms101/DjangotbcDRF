from django.db import models


class CartItemManager(models.Manager):
    def join_related_tables(self):
        return self.select_related('cart').select_related('product')
