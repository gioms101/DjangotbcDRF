import django_filters
from .models import Product, ProductTag


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='contains')
    price = django_filters.NumberFilter(lookup_expr='lte')
    tags = django_filters.ModelMultipleChoiceFilter(field_name='tags',
                                                    queryset=ProductTag.objects.all(),
                                                    to_field_name='id',
                                                    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'tags']
