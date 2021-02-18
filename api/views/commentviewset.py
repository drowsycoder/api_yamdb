from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from  rest_framework.pagination import PageNumberPagination


from ..models.review import Review
from ..serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
