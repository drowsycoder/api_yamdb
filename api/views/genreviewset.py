from rest_framework import filters, mixins, permissions, viewsets

from api.custom_permissions import IsAdminRoleOrSuperuser
from api.models import Genre
from api.serializers import GenreSerializer


class GenreViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """Представление для взаимодействия (CRUD) с жанром произведения."""
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', ]
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminRoleOrSuperuser]
        return [permission() for permission in permission_classes]
