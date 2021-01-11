from django.db import models
from django.contrib.auth.models import AbstractUser
import time

# Create your models here.
def upload_avatar(instance, filename):
    lastDot = filename.rfind('.')
    extension = filename[lastDot:len(filename):1]
    return 'images/user/%s-%s-%s' % (instance.username, time.time(), extension)

class BaseUser(AbstractUser):
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.FileField(upload_to=upload_avatar,null=True, blank=True)
    money = models.PositiveIntegerField(null=True, blank=True, default=100)
