# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostparameter',
            name='host',
        ),
        migrations.RemoveField(
            model_name='swindletest',
            name='host',
        ),
        migrations.RemoveField(
            model_name='swindletest',
            name='user',
        ),
        migrations.DeleteModel(
            name='Host',
        ),
        migrations.DeleteModel(
            name='HostParameter',
        ),
        migrations.DeleteModel(
            name='SwindleTest',
        ),
    ]
