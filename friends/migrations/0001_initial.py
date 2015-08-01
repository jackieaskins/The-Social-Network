# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('response_date', models.DateTimeField(blank=True)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friendship_set')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friends')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
