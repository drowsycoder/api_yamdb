from rest_framework import serializers

from . import CategorySerializer, GenreSerializer
from ..models import Category, Genre, Title


class CustomTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'


class TitleGetSerializer(CustomTitleSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(read_only=True, required=False)


class TitlePostSerializer(CustomTitleSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )
