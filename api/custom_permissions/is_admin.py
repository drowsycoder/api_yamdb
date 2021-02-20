from rest_framework import permissions


class IsAdminRoleOrSuper(permissions.BasePermission):
    """
    Global permission check if user is admin
    """

    def has_permission(self, request, view):
        user = request.user
        if user.is_anonymous:
            return False
        return user.is_superuser or user.role == 'admin'
