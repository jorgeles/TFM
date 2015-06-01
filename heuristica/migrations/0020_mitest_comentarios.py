# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0019_resultados_propietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitest',
            name='comentarios',
            field=models.CharField(default=datetime.datetime(2015, 6, 1, 13, 8, 47, 734815, tzinfo=utc), max_length=200000),
            preserve_default=False,
        ),
    ]
