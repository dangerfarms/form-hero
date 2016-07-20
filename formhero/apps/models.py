from django.db import models
from django.contrib.postgres.fields import ArrayField

class App(models.Model):
    name = models.TextField()
    host_list = ArrayField(models.CharField(max_length=100), default=[])
