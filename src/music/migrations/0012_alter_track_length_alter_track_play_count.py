# Generated by Django 4.1.6 on 2023-03-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0011_alter_album_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="length",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="track",
            name="play_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]