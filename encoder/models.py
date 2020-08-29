from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to="/uploads")
    base64 = models.CharField()
    md5 = models.CharField()