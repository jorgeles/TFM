# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0005_heuristica'),
    ]

    operations = [
        migrations.AddField(
            model_name='heuristica',
            name='elementos',
            field=models.CharField(default=datetime.datetime(2015, 5, 5, 8, 0, 19, 330767, tzinfo=utc), max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heuristica',
            name='rango',
            field=models.CharField(default=datetime.datetime(2015, 5, 5, 8, 0, 27, 698034, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
