from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from taggit.managers import TaggableManager

# Create your models here.

class Reference(models.Model):

    title = models.CharField(max_length=250)
    description = models.TextField()
    link = models.URLField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'desc_posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.title
