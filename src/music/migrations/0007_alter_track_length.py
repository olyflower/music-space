# Generated by Django 4.1.6 on 2023-02-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0006_alter_track_artist_alter_track_create_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="length",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
