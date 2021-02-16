from django.db.models import Avg
from rest_framework import serializers

from ..models import Category, Genre, Review, Title


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(read_only=True)
    category = CustomSlugRelatedField(queryset=Category.objects.all(),
                                      slug_field='slug')
    genre = CustomSlugRelatedField(queryset=Genre.objects.all(),
                                   slug_field='slug',
                                   many=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year',
                  'rating', 'description',
                  'genre', 'category')
