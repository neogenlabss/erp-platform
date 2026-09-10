from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Permission, Role
from .permissions import IsActiveUser,HasRBACPermission
from .serializers import PermissionSerializer, RoleSerializer
from .services import (
    assign_permissions_to_role,
    create_permission,
    create_role,
    delete_role,
    remove_permissions_from_role,
    update_role,
)


class RoleListCreateView(APIView):
    permission_classes = [IsActiveUser,HasRBACPermission]

    def get(self, request):
        roles = Role.objects.filter(is_active=True)
        serializer = RoleSerializer(roles, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        role = create_role(
            name=serializer.validated_data["name"],
            description=serializer.validated_data.get("description", ""),
            is_active=serializer.validated_data.get("is_active", True),
        )

        return Response(
            RoleSerializer(role).data,
            status=status.HTTP_201_CREATED,
        )


class RoleDetailView(APIView):
    permission_classes = [IsActiveUser]

    def get_object(self, role_id):
        return Role.objects.get(id=role_id)

    def get(self, request, role_id):
        role = self.get_object(role_id)
        return Response(RoleSerializer(role).data)

    def put(self, request, role_id):
        role = self.get_object(role_id)

        serializer = RoleSerializer(
            role,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        role = update_role(
            role,
            name=serializer.validated_data.get("name"),
            description=serializer.validated_data.get("description"),
            is_active=serializer.validated_data.get("is_active"),
        )

        return Response(RoleSerializer(role).data)

    def delete(self, request, role_id):
        role = self.get_object(role_id)
        role = delete_role(role)

        return Response(
            {"detail": "Role deactivated successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


class PermissionListCreateView(APIView):
    permission_classes = [IsActiveUser]

    def get(self, request):
        permissions = Permission.objects.filter(is_active=True)
        serializer = PermissionSerializer(permissions, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PermissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        permission = create_permission(
            name=serializer.validated_data["name"],
            codename=serializer.validated_data["codename"],
            description=serializer.validated_data.get("description", ""),
            is_active=serializer.validated_data.get("is_active", True),
        )

        return Response(
            PermissionSerializer(permission).data,
            status=status.HTTP_201_CREATED,
        )


class RolePermissionView(APIView):
    permission_classes = [IsActiveUser]

    def post(self, request, role_id):
        role = Role.objects.get(id=role_id)

        permission_ids = request.data.get("permission_ids", [])

        permissions = Permission.objects.filter(
            id__in=permission_ids,
            is_active=True,
        )

        assign_permissions_to_role(role, permissions)

        return Response(
            RoleSerializer(role).data,
            status=status.HTTP_200_OK,
        )

    def delete(self, request, role_id):
        role = Role.objects.get(id=role_id)

        permission_ids = request.data.get("permission_ids", [])

        permissions = Permission.objects.filter(
            id__in=permission_ids,
        )

        remove_permissions_from_role(role, permissions)

        return Response(
            RoleSerializer(role).data,
            status=status.HTTP_200_OK,
        )