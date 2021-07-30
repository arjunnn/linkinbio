# Generated by Django 3.2.5 on 2021-07-27 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0006_rename_url_link_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="image",
            field=models.ImageField(
                null=True, upload_to="images/", verbose_name="icon"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                null=True, upload_to="images/", verbose_name="icon"
            ),
        ),
    ]