from rest_framework import serializers

from ..models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')
    review = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='score')

    class Meta:
        model = Comment
        fields = '__all__'
