# Generated by Django 4.1.6 on 2023-03-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0006_remove_userprofile_city_remove_userprofile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="avatars/"),
        ),
    ]