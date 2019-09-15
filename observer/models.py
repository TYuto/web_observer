from django.db import models

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(max_length=30)
    is_secret = models.BooleanField()

class Version(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    html = models.TextField(max_length=100000)
    text = models.TextField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)