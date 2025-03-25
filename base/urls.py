from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAdminUser

# Swagger Config
schema_view = get_schema_view(
    openapi.Info(
        title="Old Polish API",
        default_version="v1",
        description="Dokumentacja API do staropolskich vs nowoczesnych polskich zwrotów",
    ),
    public=False,
    permission_classes=[IsAdminUser],  # superuser only
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tonguetwister.urls")),

    # Swagger UI
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

    # ReDoc
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # OpenAPI JSON
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]

# Custom error handler for 404 errors
handler404 = "tonguetwister.views.error_404_view"
