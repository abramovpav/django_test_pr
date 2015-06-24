from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    rating = models.FloatField()
