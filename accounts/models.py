from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser):
    STATUS = [
        ('verified', 'Verified'),
        ('regular', 'Regular')
    ]
    status = models.CharField(choices=STATUS, default='regular', max_length=9)
    email = models.EmailField(unique=True)

    # Set the email field as the USERNAME_FIELD for authentication
    USERNAME_FIELD = 'email'
    # Add 'email' to the REQUIRED_FIELDS for the createsuperuser command
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
