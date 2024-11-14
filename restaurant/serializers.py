from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Restaurant, MainMenuCategory, SubMenuCategory, Dish, Ingredient
from user.models import CustomUser


class ListingRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name')


class CreateRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'phone_number', 'photo')


class ListingMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMenuCategory
        fields = ('id', 'name')


class CreateMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMenuCategory
        fields = ('name', 'restaurant')


class CreateSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenuCategory
        fields = ('name', 'photo', 'main_category')


class DetailSubCategorySerializer(serializers.ModelSerializer):
    dishes = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()

    class Meta:
        model = SubMenuCategory
        fields = ('dishes', 'photos')

    def get_dishes(self, obj):
        list = []
        for dish in obj.dishes.all():
            exm = {dish.name: []}
            for ingredient in dish.ingredients.all():
                exm[dish.name].append(ingredient.name)
            list.append(exm)
        return list

    def get_photos(self, obj):
        return [dish.photo for dish in obj.dishes.all() if dish.photo]


class ListingSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenuCategory
        fields = ('name', 'photo')


class CreateDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'photo', 'price', 'sub_category')


class CreateDishIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'dish')


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     validators=[validate_password],
                                     style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True,
                                             required=True,
                                             validators=[validate_password],
                                             style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = CustomUser.objects.create_user(**validated_data)
        return user
