# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0016_resultados'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Resultados',
        ),
        migrations.AddField(
            model_name='asignados',
            name='respuestas',
            field=models.CharField(default=datetime.datetime(2015, 5, 23, 8, 52, 38, 577375, tzinfo=utc), max_length=200000),
            preserve_default=False,
        ),
    ]
