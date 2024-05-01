from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

if settings.DEBUG:
    url = "http://127.0.0.1:8000"
else:
    url = "https://aqoldi.com"

schema_view = get_schema_view(
    openapi.Info(
        title="Aqoldi Backend",
        default_version="v1",
        description="Aqoldi backend(E-commerce,Job,Blog)",
        terms_of_service="https://aqoldi.com/terms/",
        contact=openapi.Contact(name="Developers", url="https://t.me/+qs6x9r_O3Ww0ODg0"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    url=url,
)

urlpatterns = [
    # default
    path("aaadmin/", admin.site.urls),
    # Third Party
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # Mine
    path('auth/', include('authentication.urls')),

]
if not settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^static/(?:.*)$",
            serve,
            {
                "document_root": settings.STATIC_ROOT,
            },
        )
    ]
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
