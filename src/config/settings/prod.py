import os

from config.settings.base import *  # noqa

DEBUG = True

SECRET_KEY = "django-secret-key"

ALLOWED_HOSTS = ["localhost"]

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = BASE_DIR / "static_cl/"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "media_cl/"
MEDIA_URL = "/media/"

DATABASES = {
    "default_local": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "yudina_olga_db",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": 5432,
    },
    "default_sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    },
}
