from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, null= True)
    roll = models.IntegerField(null=True)
    city = models.CharField(max_length=100, null=True)

    # def __str__(self):
    #     return self.name

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender,instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
        
    