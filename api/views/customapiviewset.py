from rest_framework import filters, mixins, permissions, viewsets

from api.custom_permissions import IsAdminRoleOrSuperuser


class CustomAPIViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    """Базовый суперкласс представления для работы с CRUD.

    Используется для взаимодействия с жанром и категорией произведения.
    """
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', ]
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminRoleOrSuperuser]
        return [permission() for permission in permission_classes]
