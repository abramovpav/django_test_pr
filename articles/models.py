from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=1024)
    author = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
