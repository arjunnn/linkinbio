from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import UserSerializer, LinkSerializer, ProfileSerializer
from ..links.models import Link, Profile


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
