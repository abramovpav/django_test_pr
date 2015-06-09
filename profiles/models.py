from django.conf import settings
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    rating = models.FloatField()
