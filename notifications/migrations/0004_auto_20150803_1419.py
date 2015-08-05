# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0003_auto_20150802_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, serialize=False, to='notifications.Notification', parent_link=True, primary_key=True)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('notifications.notification',),
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='user',
            new_name='to_user',
        ),
    ]
