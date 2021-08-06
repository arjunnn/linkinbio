from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

THEME_CHOICES = (
    ("light", "🌞 light"),
    ("dark", "🌚 dark"),
    ("cupcake", "🧁 cupcake"),
    ("bumblebee", "🐝 bumblebee"),
    ("emerald", "❇ emerald"),
    ("corporate", "🏢 corporate"),
    ("synthwave", "🌃 synthwave"),
    ("retro", "👴 retro"),
    ("cyberpunk", "🤖 cyberpunk"),
    ("valentine", "🌸 valentine"),
    ("halloween", "🎃 halloween"),
    ("garden", "🌷 garden"),
    ("forest", "🌲 forest"),
    ("aqua", "🐟 aqua"),
    ("lofi", "👓 lofi"),
    ("pastel", "🖍 pastel"),
    ("‍fantasy", "🧚‍♀️ fantasy"),
    ("wireframe", "📝 wireframe"),
    ("black", "🏴 black"),
    ("luxury", "💎 luxury"),
    ("‍dracula", "🧛‍♂️ dracula"),
)


class ProfileTheme(models.Model):
    name = models.CharField(max_length=20, choices=THEME_CHOICES)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), related_name="profile", on_delete=models.CASCADE
    )
    bio = models.CharField(max_length=240)
    image = models.ImageField(verbose_name="icon", null=True, upload_to="images/")
    theme = models.ForeignKey(ProfileTheme, null=True, on_delete=models.SET_NULL)
    email_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(null=True)
    hits = models.IntegerField(default=0)

    @property
    def get_theme(self):
        if not self.theme:
            self.theme = ProfileTheme.objects.get(name="cupcake")
            self.save()
        return self.theme.name.split(" ")[1]


class Link(models.Model):
    link = models.URLField(verbose_name="URL")
    name = models.CharField(max_length=256)
    image = models.ImageField(verbose_name="icon", null=True, upload_to="images/")
    profile = models.ForeignKey(
        Profile, related_name="links", on_delete=models.CASCADE, null=True
    )
    active = models.BooleanField(default=True)
    uuid = models.UUIDField(default=uuid4, db_index=True, verbose_name="UUID")
    hits = models.IntegerField(default=0)
