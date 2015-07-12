# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_remove_statuspost_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statuscomment',
            name='user',
        ),
    ]
