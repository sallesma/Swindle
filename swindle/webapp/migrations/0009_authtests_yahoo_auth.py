# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_authtests_dropbox_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtests',
            name='yahoo_auth',
            field=models.NullBooleanField(default=None),
        ),
    ]
