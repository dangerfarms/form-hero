from django.contrib.postgres.fields import JSONField
from django.db import models

from formhero.apps.models import App
from formhero.providers.dbform import Backend as DBBackend
from formhero.providers.email import Backend as EmailBackend


class Form(models.Model):
    HANDLERS = (
        ('db', DBBackend,),
        ('email', EmailBackend),
    )

    app = models.ForeignKey(App)
    name = models.TextField()
    handler = models.TextField(choices=HANDLERS)
    config = JSONField()
