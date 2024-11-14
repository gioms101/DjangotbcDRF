import django_filters
from .models import SubMenuCategory, MainMenuCategory, Dish


class CategoryFilter(django_filters.FilterSet):
    main_category = django_filters.ModelMultipleChoiceFilter(field_name='main_category',
                                                             queryset=MainMenuCategory.objects.all(),
                                                             )

    dishes = django_filters.ModelMultipleChoiceFilter(field_name='dishes',
                                                      queryset=Dish.objects.all(),
                                                      )

    class Meta:
        model = SubMenuCategory
        fields = ('main_category', 'dishes')
