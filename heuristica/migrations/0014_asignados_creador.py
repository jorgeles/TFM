# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0013_asignados'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignados',
            name='creador',
            field=models.CharField(default=datetime.datetime(2015, 5, 21, 7, 30, 15, 863069, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
