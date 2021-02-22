from django.db.models import Avg
from rest_framework import permissions, viewsets

from ..custom_permissions import IsAdminRoleOrSuper
from ..models import Title
from ..serializers import TitleGetSerializer, TitlePostSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg(
        'reviews__score')
    ).order_by('-id')
    # serializer_class = TitlePostSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['=name', ]
    filterset_fields = ['year', 'name', 'category__slug', 'genre__slug']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminRoleOrSuper]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleGetSerializer
        return TitlePostSerializer
