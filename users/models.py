from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField('номер телефона', unique=True)
    username = models.CharField('никнейм', max_length=100, unique=True)
    date_of_birth = models.DateField('Дата рождения', help_text='формат: 00.00.0000', null=True, blank=True)

    PHOME_FIELD = "phone_number"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return str(self.phone_number)
