# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dbform', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormEntry',
            new_name='FormSubmission',
        ),
    ]
