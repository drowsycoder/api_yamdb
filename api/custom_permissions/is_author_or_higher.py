from rest_framework import permissions


class IsAuthorOrHigher(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (request.method in permissions.SAFE_METHODS
                or user.is_superuser or user.role == 'admin' or
                obj.author == user)
