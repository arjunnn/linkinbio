import json

from django.contrib.auth import get_user_model
from rest_framework import viewsets, response

from .serializers import (
    UserSerializer,
    LinkSerializer,
    ProfileSerializer,
    ProfileThemeSerializer,
)
from ..links.models import Link, Profile, ProfileTheme, THEME_CHOICES


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileThemeViewSet(viewsets.ModelViewSet):
    queryset = ProfileTheme.objects.all()
    serializer_class = ProfileThemeSerializer
    http_method_names = ['get']

    def list(self, *args, **kwargs):
        return response.Response([theme[0] for theme in THEME_CHOICES])

