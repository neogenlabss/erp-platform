from django.urls import path

from .views import (
    PermissionListCreateView,
    RoleDetailView,
    RoleListCreateView,
    RolePermissionView,
)

urlpatterns = [
    path("roles/", RoleListCreateView.as_view(), name="role-list-create"),
    path("roles/<int:role_id>/", RoleDetailView.as_view(), name="role-detail"),

    path(
        "permissions/",
        PermissionListCreateView.as_view(),
        name="permission-list-create",
    ),

    path(
        "roles/<int:role_id>/permissions/",
        RolePermissionView.as_view(),
        name="role-permissions",
    ),
]