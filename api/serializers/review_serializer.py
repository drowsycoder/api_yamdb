from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..models.review import Review
from ..models.user import User
from ..models.title import Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')
    title = serializers.SlugRelatedField(many=False, read_only=True,
                                         slug_field='name')

    class Meta:
        model = Review
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['author', 'title']
            )
        ]
