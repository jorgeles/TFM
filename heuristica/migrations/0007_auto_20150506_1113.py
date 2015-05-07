# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0006_auto_20150505_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='heuristica',
            name='atributos',
            field=models.CharField(default=datetime.datetime(2015, 5, 6, 11, 13, 30, 658239, tzinfo=utc), max_length=20000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='heuristica',
            name='elementos',
            field=models.CharField(max_length=20000),
            preserve_default=True,
        ),
    ]
