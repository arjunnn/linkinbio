# Generated by Django 3.2.5 on 2021-07-30 22:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0014_auto_20210731_0405"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Redirect",
        ),
        migrations.AddField(
            model_name="link",
            name="hits",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="link",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.UUID("0d109519-0015-4b7a-87e3-3ab70abe9914"),
                verbose_name="UUID",
            ),
        ),
    ]
