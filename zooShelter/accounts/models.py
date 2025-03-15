from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from zooShelter.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=100,
        unique=True
    )

    email = models.EmailField(
        unique=True
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    nickname = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    bio = models.TextField(
        null=True,
        blank=True
    )

    website = models.URLField(
        null=True,
        blank=True
    )

    social_media_account = models.URLField(
        null=True,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        null=True,
        blank=True
    )

    def get_display_name(self):
        return self.nickname or self.first_name or self.user.username
