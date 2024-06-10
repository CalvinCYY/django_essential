from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField(max_length=75, unique=True)
    date = models.DateTimeField(auto_now_add=True)