from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    # human readable, first 50 characters
    def __str__(self):
        return self.text[:50]