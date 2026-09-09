from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    message = "Your account is inactive."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_active
        )