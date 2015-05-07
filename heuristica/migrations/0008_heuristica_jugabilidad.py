# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0007_auto_20150506_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='heuristica',
            name='jugabilidad',
            field=models.CharField(default=datetime.datetime(2015, 5, 6, 15, 8, 51, 826779, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
    ]
