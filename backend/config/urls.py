from django.urls import include, path

urlpatterns = [
    path("api/rbac/", include("modules.rbac.urls")),
]