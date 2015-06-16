# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0020_mitest_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='heuristica',
            name='comentarioVisible',
            field=models.CharField(default=datetime.datetime(2015, 6, 16, 7, 3, 42, 955701, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
    ]
