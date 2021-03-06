# Generated by Django 3.2.5 on 2021-07-30 22:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0013_alter_redirect_uuid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="redirect",
            old_name="counter",
            new_name="hits",
        ),
        migrations.AddField(
            model_name="profile",
            name="hits",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="profile",
            name="last_updated",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="redirect",
            name="uuid",
            field=models.UUIDField(
                db_index=True,
                default=uuid.UUID("3d9c6842-9968-4b04-9395-cc91c8fe8b41"),
                primary_key=True,
                serialize=False,
                verbose_name="UUID",
            ),
        ),
    ]
