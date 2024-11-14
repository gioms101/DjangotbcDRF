from rest_framework import serializers
from .models import Product


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


class SendEmailSerializer(serializers.Serializer):
    subject = serializers.CharField(required=True, write_only=True)
    message = serializers.CharField(required=True, write_only=True)
