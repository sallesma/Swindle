# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_authtests_facebook_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtests',
            name='twitter_auth',
            field=models.NullBooleanField(default=None),
        ),
    ]
