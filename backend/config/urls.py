from django.urls import include, path

urlpatterns = [
    path("api/users/", include("modules.accounts.urls")),
    path("api/auth/", include("modules.rbac.urls")),
    path("api/rbac/", include("modules.rbac.urls")),
    path("api/rbac/", include("modules.rbac.urls")),
]