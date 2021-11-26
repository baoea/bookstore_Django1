from categories.views import CategoryViewSet
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from rest_framework import routers

api_router = routers.SimpleRouter()
api_router.register(r"categories", CategoryViewSet, basename="categories")


urlpatterns = [
    path("", RedirectView.as_view(url="admin/")),
    re_path(r"^api/", include((api_router.urls, "api"), namespace="api")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
