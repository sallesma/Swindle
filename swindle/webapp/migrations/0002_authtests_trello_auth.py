# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_user_and_basic_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtests',
            name='trello_auth',
            field=models.NullBooleanField(default=None),
        ),
    ]
