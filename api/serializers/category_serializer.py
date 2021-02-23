from rest_framework import serializers

from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели категории произведения (Category)."""

    class Meta:
        model = Category
        fields = ['name', 'slug']
