from django.db import models
from accounts.models import Account
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Post(models.Model):
    PRIVACY=[
        ('Everyone','Everyone'),
        ('Nobody','Nobody'),
        ('Friends','Friends')
    ]
    author=models.ForeignKey(Account,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    slug=models.SlugField(null=True,blank=True)
    privacy=models.CharField(choices=PRIVACY,default='Friends',max_length=20)
    
    
    def __str__(self):
        return self.author.username
    
@receiver(post_save,sender=Post)
def create(sender,created,instance,**kwargs):
    if created:
        slug=slugify(instance.title)
        instance.slug=slug
        instance.save()