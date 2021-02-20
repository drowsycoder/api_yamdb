from rest_framework import serializers

from ..models import Category, Genre, Title


class TitleSerializer(serializers.ModelSerializer):
    # rating = serializers.SerializerMethodField(read_only=True)
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )

    class Meta:
        model = Title
        fields = '__all__'
