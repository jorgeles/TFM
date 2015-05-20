# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0009_mitest'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitest',
            name='seleccionados',
            field=models.CharField(default=datetime.datetime(2015, 5, 16, 8, 48, 30, 601182, tzinfo=utc), max_length=2000),
            preserve_default=False,
        ),
    ]
