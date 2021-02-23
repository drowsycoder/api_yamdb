from rest_framework import permissions


class IsAdminRoleOrSuper(permissions.BasePermission):
    """Проверка на наличие роли 'admin' или прав суперпользователя"""

    def has_permission(self, request, view) -> bool:
        user = request.user
        if user.is_anonymous:
            return False
        return user.is_superuser or user.role == 'admin'
