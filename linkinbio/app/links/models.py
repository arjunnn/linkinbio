from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), related_name="profile", on_delete=models.CASCADE
    )
    bio = models.CharField(max_length=240)
    image = models.ImageField(verbose_name="icon", null=True, upload_to="images/")


class Link(models.Model):
    link = models.URLField(verbose_name="URL")
    name = models.CharField(max_length=256)
    image = models.ImageField(verbose_name="icon", null=True, upload_to="images/")
    profile = models.ForeignKey(
        Profile, related_name="links", on_delete=models.CASCADE, null=True
    )
    active = models.BooleanField(default=True)
