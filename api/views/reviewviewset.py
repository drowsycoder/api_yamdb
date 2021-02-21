from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models.title import Title
from ..serializers import ReviewSerializer
from ..custom_permissions import IsAuthorOrHigher


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrHigher]
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
