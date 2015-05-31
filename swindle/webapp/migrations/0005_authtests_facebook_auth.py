# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20150522_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtests',
            name='facebook_auth',
            field=models.NullBooleanField(default=None),
        ),
    ]
