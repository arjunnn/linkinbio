from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, ProfileViewSet, LinkViewSet, ProfileThemeViewSet

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"links", LinkViewSet)
router.register(r"profiles", ProfileViewSet)
router.register(r"themes", ProfileThemeViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
