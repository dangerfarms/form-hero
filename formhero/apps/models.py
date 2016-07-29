from django.contrib.postgres.fields import ArrayField
from django.db import models


class App(models.Model):
    name = models.TextField()
    host_list = ArrayField(models.CharField(max_length=100), blank=True, default=[])
