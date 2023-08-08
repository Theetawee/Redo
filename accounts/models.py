from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import os
# Create your models here.


class Account(AbstractUser):
    STATUS = [
        ('verified', 'Verified'),
        ('regular', 'Regular')
    ]
    status = models.CharField(choices=STATUS, default='regular', max_length=9)
    email = models.EmailField(unique=True)
    phone=PhoneNumberField(null=True,blank=True)
    verified_email=models.BooleanField(default=False)
    slug=models.SlugField(null=True,blank=True,unique=True)
    profile_image=models.ImageField(upload_to='profiles/',null=True,blank=True)
    

    # Set the email field as the USERNAME_FIELD for authentication
    USERNAME_FIELD = 'username'
    # Add 'email' to the REQUIRED_FIELDS for the createsuperuser command
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    @property
    def image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            url=os.path.join(settings.STATIC_URL,'images','default.webp')
            return url

@receiver(post_save,sender=Account)
def create_slug(sender,instance,created,**kwargs):
    if created:
        slug=slugify(instance.username)
        instance.slug=slug
        instance.save()