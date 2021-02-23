from rest_framework import filters, mixins, permissions, viewsets

from api.custom_permissions import IsAdminRoleOrSuper
from api.models import Category
from api.serializers import CategorySerializer


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """Представление для взаимодействия (CRUD) с категорией произведения."""
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', ]
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminRoleOrSuper]
        return [permission() for permission in permission_classes]
