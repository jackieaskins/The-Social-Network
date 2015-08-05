# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_auto_20150729_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Pending...'), (1, 'Friends')], default=0),
        ),
    ]
