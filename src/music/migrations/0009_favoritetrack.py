# Generated by Django 4.1.6 on 2023-03-24 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("music", "0008_artist_alter_album_options_alter_genre_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FavoriteTrack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                (
                    "track",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="music.track"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
