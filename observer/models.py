from django.db import models
import uuid
# Create your models here.

class Site(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    key = models.CharField(max_length=30)
    password = models.CharField(max_length=30, blank=True, null=True)
    url = models.CharField(max_length=100, default="")
    is_secret = models.BooleanField()
    def __str__(self):
        return self.name

class Version(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    html = models.TextField(max_length=100000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.site.name + ':' + self.updated_at.strftime('%Y/%m/%d')

class Notify(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    key = models.CharField(max_length=30)
    url = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.site.name + ':' + self.key