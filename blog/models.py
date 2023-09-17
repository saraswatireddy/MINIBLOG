from django.db import models

# Create your models
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
