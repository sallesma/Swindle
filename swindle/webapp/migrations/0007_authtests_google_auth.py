# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_authtests_twitter_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtests',
            name='google_auth',
            field=models.NullBooleanField(default=None),
        ),
    ]
