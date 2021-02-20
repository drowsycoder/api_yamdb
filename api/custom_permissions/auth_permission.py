from rest_framework import permissions

from ..models import EmailAuth


class EmailCodeCorrectPermission(permissions.BasePermission):
    """
    Global permission check for correct email and confirmation code.
    """

    def has_permission(self, request, view):
        email = request.POST['email']
        confirmation_code = request.POST['confirmation_code']
        correct_auth_data = EmailAuth.objects.filter(
            email=email, confirmation_code=confirmation_code
        ).exists()
        return correct_auth_data
