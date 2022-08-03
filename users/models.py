from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from school.models import Teacher
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    user = models.OneToOneField(Teacher, on_delete=models.PROTECT, verbose_name='пользоваель')
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
