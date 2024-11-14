from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterPage, RestaurantPage, MenuPageView, SubCategoryViewSet, CreateDishViewSet, \
    CreateIngredientViewSet

restaurant_router = DefaultRouter()
restaurant_router.register(r'main', RestaurantPage)
restaurant_router.register(r'subcategory', SubCategoryViewSet)
restaurant_router.register(r'dish', CreateDishViewSet)
restaurant_router.register(r'ingredient', CreateIngredientViewSet)

urlpatterns = [
    path('menu/', MenuPageView.as_view(), name='menu-page'),
    path('register/', RegisterPage.as_view(), name='register-page'),
    path('', include(restaurant_router.urls)),
]
