from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User)

    # @property
    # def id(self):
    #     return '{}'.format(self.user)
    #
    # def __str__(self):
    #     return self.id
    #
    # def __str__(self):
    #     return self.title
    #
    # class Meta:
    #     ordering = ['title']


PRIORITY = (
    (1, 'Low priority'),
    (2, 'Normal priority'),
    (3, 'High priority'),
)


class Item(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now())
    priority = models.IntegerField(choices=PRIORITY)
    completed = models.BooleanField(default=False)
    list = models.ForeignKey(List)

    # def __str__(self):
    #     return self.title
