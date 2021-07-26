from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..links.models import Link, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ["url", "link", "name", "image", "active"]


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["user", "bio", "links", "image"]
