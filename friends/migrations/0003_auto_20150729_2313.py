# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20150729_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='response_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
