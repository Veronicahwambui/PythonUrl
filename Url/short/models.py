from django.db import models

# Create your models here.
class Short_urls(models.Model):
    short_url=models.CharField(max_length=201)
    long_url=models.URLField("URL",unique=True)
