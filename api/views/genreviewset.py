from rest_framework import filters, viewsets

from ..models.genre import Genre
from ..serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', ]
