# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0009_auto_20150715_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statuscomment',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='statuspost',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='statuscomment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statuspost',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
