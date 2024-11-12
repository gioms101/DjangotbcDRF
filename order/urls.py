from django.urls import path
from .views import CartPage, AddToCartView, DeleteCartItemView

app_name = 'order'

urlpatterns = [
    path('cart/', CartPage.as_view(), name='cart'),
    path('add/', AddToCartView.as_view(), name='add_cart'),
    path('delete/<int:product_id>/', DeleteCartItemView.as_view(), name='delete_cart'),
]
