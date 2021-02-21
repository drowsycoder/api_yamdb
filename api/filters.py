from django_filters import CharFilter, rest_framework as filters

from .models import Title


class NumberRangeFilter(filters.FilterSet):
    genre = CharFilter(field_name='genre__slug', lookup_expr='iexact')
    category = CharFilter(field_name='category__slug', lookup_expr='iexact')

    class Meta:
        model = Title
        fields = ['genre', 'category']
