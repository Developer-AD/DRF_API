from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# Create your models here.


class MyUser(AbstractUser):

    # username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    # def __str__(self):
    #     return self.username

class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    # mobile = models.IntegerField(null=True, blank=True)
    # image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    verified = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.full_name

def create_user_profile(sender, instance, created,*args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, *args, **kwargs):
    instance.profile.save()

# post_save.connect(create_user_profile, sender=MyUser)
# post_save.connect(save_user_profile, sender=MyUser)



# class Database(models.Model):
#     user = models.ForeignKey(
#         MyUser, on_delete=models.CASCADE, default=None, blank=True, null=True)
#     db_name = models.CharField(max_length=50, blank=True, null=True)
#     creation_date = models.DateField(default=None, blank=True, null=True)
#     db_data = models.CharField(max_length=5000000, blank=True, null=True)
#     db_records = models.IntegerField(default=0, blank=True, null=True)

#     def __str__(self):
#         return self.db_name