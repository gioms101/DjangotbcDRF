from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import CartItem
from .serializers import CartItemSerializer, AddToCartItemSerializer

# Create your views here.


class CartPage(ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.join_related_tables().filter(cart_id=self.request.user.id)


class AddToCartView(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = AddToCartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart = self.request.user.cart
        product = serializer.validated_data['product']
        cart_item_obj = CartItem.objects.filter(cart=cart, product=product)
        if cart_item_obj.exists():
            cart_item_obj = cart_item_obj.first()
            cart_item_obj.quantity += 1
            cart_item_obj.save(update_fields=['quantity'])
        else:
            serializer.save(cart=cart)


class DeleteCartItemView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart = self.request.user.cart
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(CartItem, cart=cart, product_id=product_id)
