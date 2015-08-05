# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20150802_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Unread'), (1, 'Read'), (2, 'Complete')], default=0),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type_id',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Friend Request'), (1, 'Message')]),
        ),
    ]
