from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..custom_permissions import IsAdminRoleorSuper
from ..models import User
from ..serializers import MeUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminRoleorSuper]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'username',
    ]

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        user = get_object_or_404(self.queryset, username=request.user.username)
        if request.method == 'GET':

            serializer = MeUserSerializer(user)
            return Response(serializer.data)
        if request.method == 'PATCH':
            serializer = MeUserSerializer(
                user, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
