# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0003_juegos'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegos',
            name='propietario',
            field=models.CharField(default=datetime.datetime(2015, 4, 21, 10, 33, 54, 81860, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
