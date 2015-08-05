# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20150803_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='from_user',
            field=models.ForeignKey(related_name='sent_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
