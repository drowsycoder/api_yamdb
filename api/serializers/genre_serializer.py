from rest_framework import serializers

from ..models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели жанра произведения (Genre)."""

    class Meta:
        model = Genre
        fields = ['name', 'slug']
