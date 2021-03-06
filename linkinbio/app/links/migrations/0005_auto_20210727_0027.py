# Generated by Django 3.2.5 on 2021-07-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0004_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="image",
            field=models.ImageField(
                null=True, upload_to="static/", verbose_name="icon"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                null=True, upload_to="static/", verbose_name="icon"
            ),
        ),
    ]
