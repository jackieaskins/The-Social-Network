# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150711_0048'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0003_statuspost'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusComment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='statuspost',
            name='update_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AddField(
            model_name='statuscomment',
            name='status_post',
            field=models.ForeignKey(to='network.StatusPost'),
        ),
        migrations.AddField(
            model_name='statuscomment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='statuscomment',
            name='user_profile',
            field=models.ForeignKey(to='profiles.UserProfile'),
        ),
    ]
