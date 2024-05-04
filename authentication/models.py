import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Users(AbstractUser):
    UserId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?09?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            ),
        ]
    )
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='user_image', null=True,blank=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
