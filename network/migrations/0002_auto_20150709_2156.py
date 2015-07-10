# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuspost',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='statuspost',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
