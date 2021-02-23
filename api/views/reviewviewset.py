from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..custom_permissions import IsAuthorOrHigherOrReadOnly
from ..models import Title
from ..serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Представление для взаимодействия (CRUD) с отзывами."""

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsAuthorOrHigherOrReadOnly]
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all().order_by('pub_date')

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
