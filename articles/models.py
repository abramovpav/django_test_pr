from django.conf import settings
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=1024)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
