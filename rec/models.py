from django.db import models
from django.utils import timezone

# Create your models here.

class Notifications(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    heading = models.CharField(max_length=256)
    content = models.CharField(max_length=2048)
    link = models.CharField(max_length=512)
    updatedby = models.CharField(max_length=256)

    def __str__(self):
        return self.heading