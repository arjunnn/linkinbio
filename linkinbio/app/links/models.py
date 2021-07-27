from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

THEME_CHOICES = (
    ("light", "light"),
    ("dark", "dark"),
    ("cupcake", "cupcake"),
    ("bumblebee", "bumblebee"),
    ("emerald", "emerald"),
    ("corporate", "corporate"),
    ("synthwave", "synthwave"),
    ("retro", "retro"),
    ("cyberpunk", "cyberpunk"),
    ("valentine", "valentine"),
    ("halloween", "halloween"),
    ("garden", "garden"),
    ("forest", "forest"),
    ("aqua", "aqua"),
    ("lofi", "lofi"),
    ("pastel", "pastel"),
    ("fantasy", "fantasy"),
    ("wireframe", "wireframe"),
    ("black", "black"),
    ("luxury", "luxury"),
    ("dracula", "dracula"),
)


class ProfileTheme(models.Model):
    name = models.CharField(max_length=20, choices=THEME_CHOICES)


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), related_name="profile", on_delete=models.CASCADE
    )
    bio = models.CharField(max_length=240)
    image = models.ImageField(verbose_name="icon", null=True, upload_to="images/")
    theme = models.ForeignKey(ProfileTheme, null=True, on_delete=models.SET_NULL)


class Link(models.Model):
    link = models.URLField(verbose_name="URL")
    name = models.CharField(max_length=256)
    image = models.ImageField(verbose_name="icon", null=True, upload_to="images/")
    profile = models.ForeignKey(
        Profile, related_name="links", on_delete=models.CASCADE, null=True
    )
    active = models.BooleanField(default=True)
