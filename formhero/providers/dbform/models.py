from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models

from formhero.forms.models import Form


class FormSubmission(models.Model):
    form = models.ForeignKey(Form)
    form_data = JSONField()
