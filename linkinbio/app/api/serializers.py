from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..links.models import Link, Profile, THEME_CHOICES, ProfileTheme


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ["url", "link", "name", "image", "active"]


class ProfileThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileTheme
        fields = ["name"]


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    theme = ProfileThemeSerializer()

    class Meta:
        model = Profile
        fields = ["url", "user", "bio", "links", "image", "theme"]

    def update(self, instance, validated_data):
        name = validated_data.get("theme").get("name")
        theme, created = ProfileTheme.objects.get_or_create(name=name)
        instance.theme = theme
        instance.save()
        return instance
