# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20150711_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statuspost',
            name='user',
        ),
    ]
