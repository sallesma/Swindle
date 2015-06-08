# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_authtests_yahoo_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtests',
            name='live_auth',
            field=models.NullBooleanField(default=None),
        ),
    ]
