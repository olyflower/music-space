# Generated by Django 4.1.6 on 2023-04-08 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0012_alter_track_length_alter_track_play_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="album",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tracks",
                to="music.album",
            ),
        ),
        migrations.AlterField(
            model_name="track",
            name="artist",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="artist",
                to="music.artist",
            ),
        ),
    ]
