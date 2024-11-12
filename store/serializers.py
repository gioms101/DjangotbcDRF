from django.contrib.auth import login
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Product
from order.models import CartItem, UserCard
from user.models import CustomUser


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ['description']

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]


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


class SendEmailSerializer(serializers.Serializer):
    subject = serializers.CharField(required=True, write_only=True)
    message = serializers.CharField(required=True, write_only=True)
