from rest_framework import serializers

from ..models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')
    title = serializers.SlugRelatedField(many=False, read_only=True,
                                         slug_field='name')

    class Meta:
        model = Review
        fields = '__all__'
