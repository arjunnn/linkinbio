# Generated by Django 3.2.5 on 2021-07-28 08:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0011_profile_theme"),
    ]

    operations = [
        migrations.CreateModel(
            name="Redirect",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.UUID("05dabba5-9ad9-4107-ae81-ee3f56c093da"),
                        primary_key=True,
                        serialize=False,
                        verbose_name="UUID",
                    ),
                ),
                ("to", models.URLField(verbose_name="URL")),
                ("counter", models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="created",
            field=models.DateTimeField(auto_now=True),
        ),
    ]