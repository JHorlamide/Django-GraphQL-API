from django.db import models

class BlogPost(models.Model):
  title = models.CharField(max_length=255, blank=True, null=True)
  author = models.CharField(max_length=255, blank=True, null=True)
  message = models.TextField(max_length=255, blank=True, null=True)