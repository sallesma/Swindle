# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_authtests_trello_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtests',
            name='linkedin_auth',
            field=models.NullBooleanField(default=None),
        ),
    ]
