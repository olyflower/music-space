from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from account.managers import CustomerManager


class Customer(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(_("name"), max_length=150, blank=True)
    last_name = models.CharField(_("surname"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    phone_number = PhoneNumberField(_("phone number"), null=True, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="media/img/profiles", blank=True)
    city = models.CharField(max_length=255, blank=True)

    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_working_time(self):
        return f"Time on site: {timezone.now() - self.date_joined}"


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    USER_TYPE_CHOICES = (
        ("User", "User"),
        ("Musician", "Musician"),
    )
    GENRE_CHOICES = (
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
    )
    user = models.OneToOneField(get_user_model(), related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="user_profile_photo/", blank=True, null=True)
    favourite_genres = models.CharField(max_length=30, choices=GENRE_CHOICES)
    website = models.URLField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=100, null=True)
