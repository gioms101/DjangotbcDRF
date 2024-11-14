import django_filters
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from .serializers import RegisterUserSerializer, ListingRestaurantSerializer, CreateRestaurantSerializer, \
    ListingMenuSerializer, CreateMenuSerializer, CreateSubCategorySerializer, ListingSubCategorySerializer, \
    CreateDishSerializer, CreateDishIngredientSerializer, DetailSubCategorySerializer
from django.contrib.auth import login
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Restaurant, MainMenuCategory, SubMenuCategory, Dish, Ingredient
from .filtersets import CategoryFilter


# Create your views here.


class RestaurantPage(ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = ListingRestaurantSerializer

    @action(detail=False, methods=['post'], serializer_class=CreateRestaurantSerializer,
            permission_classes=[IsAuthenticated])
    def add_restaurant(self, request):
        serializer = CreateRestaurantSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = request.user
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MenuPageView(ListCreateAPIView):
    queryset = MainMenuCategory.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateMenuSerializer
        return ListingMenuSerializer


class SubCategoryViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = SubMenuCategory.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = CategoryFilter
    lookup_field = 'name'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return ListingSubCategorySerializer
        elif self.action == 'retrieve':
            return DetailSubCategorySerializer
        elif self.action == 'create':
            return CreateSubCategorySerializer


class CreateDishViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Dish.objects.all()
    serializer_class = CreateDishSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'name'


class CreateIngredientViewSet(mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.RetrieveModelMixin,
                              GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = CreateDishIngredientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'name'


class RegisterPage(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)
