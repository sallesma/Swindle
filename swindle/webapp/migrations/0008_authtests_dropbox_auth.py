# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_authtests_google_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtests',
            name='dropbox_auth',
            field=models.NullBooleanField(default=None),
        ),
    ]
