from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.
    """

    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(_("username"), max_length=256, blank=True)
    firstname = models.CharField(_("first name"), max_length=256)
    lastname = models.CharField(_("last name"), max_length=256)
    middlename = models.CharField(_("middle name"), max_length=256, blank=True)
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    profile_picture = VersatileImageField(upload_to="user/profile-picture/", blank=True, null=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now, editable=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    @property
    def fullname(self):
        if self.middlename:
            return f"{self.firstname} {self.middlename} {self.lastname}"
        return f"{self.firstname} {self.lastname}"

    @property
    def shortname(self):
        return f"{self.lastname}_{self.firstname}"

    def __str__(self):
        return self.fullname
