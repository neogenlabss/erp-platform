from rest_framework.permissions import BasePermission

from .models import Permission

class IsActiveUser(BasePermission):
    message = "Your account is inactive."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_active
        )

class HasRBACPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if not request.user.is_active:
            return False

        required_permission = getattr(view, "required_permission", None)

        if not required_permission:
            return False

        return Permission.objects.filter(
            codename=required_permission,
            is_active=True,
            roles__users=request.user,
        ).exists()