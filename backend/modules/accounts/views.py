from rest_framework import generics

from modules.rbac.permissions import (
    IsActiveUser,
    HasRBACPermission,
)

from .models import User
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer

        return UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            self.required_permission = "user_create"
        else:
            self.required_permission = "user_view"

        return [
            IsActiveUser(),
            HasRBACPermission(),
        ]

    def perform_create(self, serializer):
        serializer.save()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "DELETE":
            self.required_permission = "user_delete"
        elif self.request.method in ["PUT", "PATCH"]:
            self.required_permission = "user_update"
        else:
            self.required_permission = "user_view"

        return [
            IsActiveUser(),
            HasRBACPermission(),
        ]