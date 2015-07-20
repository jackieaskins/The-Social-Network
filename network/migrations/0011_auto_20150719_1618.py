# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_auto_20150719_0235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuscomment',
            options={'ordering': ['post_date']},
        ),
        migrations.AlterModelOptions(
            name='statuspost',
            options={'ordering': ['-post_date']},
        ),
    ]
