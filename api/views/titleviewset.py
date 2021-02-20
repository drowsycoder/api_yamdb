from rest_framework import filters, viewsets

from ..models.title import Title
from ..serializers import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().order_by('name')
    serializer_class = TitleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', ]
