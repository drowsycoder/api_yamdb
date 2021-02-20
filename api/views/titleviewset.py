from rest_framework import filters, permissions, viewsets

from ..custom_permissions import IsAdminRoleorSuper
from ..models import Title
from ..serializers import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().order_by('name')
    serializer_class = TitleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', ]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminRoleorSuper]
        return [permission() for permission in permission_classes]
