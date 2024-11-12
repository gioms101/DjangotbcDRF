from django.contrib.auth import login
from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductListSerializer, RegisterUserSerializer, SendEmailSerializer
from .models import Product
from user.models import CustomUser
from .filtersets import ProductFilter


# Create your views here.

class ListPage(ListAPIView):
    queryset = Product.objects.join_related_tables()
    serializer_class = ProductListSerializer
    filterset_class = ProductFilter
    ordering_fields = ['price', 'quantity']

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        if slug:
            queryset = queryset.filter(category__name=slug)
        return queryset


class ProductDetailPage(RetrieveAPIView):
    queryset = Product.objects.join_related_tables()
    serializer_class = ProductListSerializer
    lookup_field = 'slug'


class RegisterPage(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)


class SendEmailPage(CreateAPIView):
    serializer_class = SendEmailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            send_mail(
                self.request.data.get('subject'),
                self.request.data.get('message'),
                self.request.user.email,
                [CustomUser.objects.get(username='admin').email],
                fail_silently=False,
            )
        except Exception as e:
            raise ValidationError({"message": f"An error occurred {e}"})
