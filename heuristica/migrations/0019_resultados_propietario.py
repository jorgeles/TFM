# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0018_auto_20150525_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultados',
            name='propietario',
            field=models.CharField(default=datetime.datetime(2015, 5, 25, 7, 16, 17, 205300, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
