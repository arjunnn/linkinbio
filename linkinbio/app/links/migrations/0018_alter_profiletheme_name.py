# Generated by Django 3.2.5 on 2021-08-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0017_alter_link_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profiletheme",
            name="name",
            field=models.CharField(
                choices=[
                    ("🌞 light", "🌞 light"),
                    ("🌚 dark", "🌚 dark"),
                    ("🧁 cupcake", "🧁 cupcake"),
                    ("🐝 bumblebee", "🐝 bumblebee"),
                    ("❇ emerald", "❇ emerald"),
                    ("🏢 corporate", "🏢 corporate"),
                    ("🌃 synthwave", "🌃 synthwave"),
                    ("👴 retro", "👴 retro"),
                    ("🤖 cyberpunk", "🤖 cyberpunk"),
                    ("🌸 valentine", "🌸 valentine"),
                    ("🎃 halloween", "🎃 halloween"),
                    ("🌷 garden", "🌷 garden"),
                    ("🌲 forest", "🌲 forest"),
                    ("🐟 aqua", "🐟 aqua"),
                    ("👓 lofi", "👓 lofi"),
                    ("🖍 pastel", "🖍 pastel"),
                    ("🧚\u200d♀️ fantasy", "🧚\u200d♀️ fantasy"),
                    ("📝 wireframe", "📝 wireframe"),
                    ("🏴 black", "🏴 black"),
                    ("💎 luxury", "💎 luxury"),
                    ("🧛\u200d♂️ dracula", "🧛\u200d♂️ dracula"),
                ],
                max_length=20,
            ),
        ),
    ]
