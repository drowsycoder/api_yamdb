from rest_framework import filters, viewsets, permissions

from ..models import Genre
from ..serializers import GenreSerializer
from ..custom_permissions import IsAdminRoleorSuper


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', ]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminRoleorSuper]
        return [permission() for permission in permission_classes]
