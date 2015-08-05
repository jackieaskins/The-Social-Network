# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notification_type',
        ),
        migrations.AddField(
            model_name='notification',
            name='type_id',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
