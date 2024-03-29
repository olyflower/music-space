# Generated by Django 4.1.6 on 2023-03-07 21:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0004_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="favourite_genres",
            field=models.CharField(
                choices=[
                    ("Rock", "Rock"),
                    ("Pop", "Pop"),
                    ("Hip Hop", "Hip Hop"),
                    ("Jazz", "Jazz"),
                    ("Blues", "Blues"),
                    ("Country", "Country"),
                    ("Folk", "Folk"),
                    ("Reggae", "Reggae"),
                    ("R&B", "R&B"),
                    ("Soul", "Soul"),
                    ("Funk", "Funk"),
                ],
                max_length=30,
            ),
        ),
    ]
