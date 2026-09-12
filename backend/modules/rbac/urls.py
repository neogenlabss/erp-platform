from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    PermissionListCreateView,
    RoleDetailView,
    RoleListCreateView,
    RolePermissionView,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
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