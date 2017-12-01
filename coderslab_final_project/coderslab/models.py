from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User)


PRIORITY = (
    (1, 'Low priority'),
    (2, 'Normal priority'),
    (3, 'High priority'),
)


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(default=datetime.now())
    priority = models.IntegerField(choices=PRIORITY)
    list = models.ForeignKey(List)


