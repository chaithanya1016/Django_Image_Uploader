from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    
