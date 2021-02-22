from rest_framework import serializers

from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')
    title = serializers.SlugRelatedField(many=False, read_only=True,
                                         slug_field='id')

    def validate(self, data):
        review = Review.objects.filter(
            title=self.context['view'].kwargs.get('title_id'),
            author=self.context['request'].user)
        if review.exists() and self.context['request'].method == 'POST':
            raise serializers.ValidationError('Review already exists')
        return data

    class Meta:
        model = Review
        fields = '__all__'
