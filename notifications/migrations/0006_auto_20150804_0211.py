# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_auto_20150803_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, 'Unread'), (1, 'Read')]),
        ),
    ]
