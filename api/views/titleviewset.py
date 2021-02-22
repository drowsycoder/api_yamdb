from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter

from ..custom_permissions import IsAdminRoleOrSuper
from ..filters import TitleFilter
from ..models import Title
from ..serializers import TitleGetSerializer, TitlePostSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg(
        'reviews__score')
    ).order_by('-id')
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TitleFilter
    search_fields = ['=name', ]

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminRoleOrSuper]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleGetSerializer
        return TitlePostSerializer  # 'create', 'update', 'partial_update'
