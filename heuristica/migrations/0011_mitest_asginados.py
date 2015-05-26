# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0010_mitest_seleccionados'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitest',
            name='asginados',
            field=models.CharField(default=datetime.datetime(2015, 5, 20, 14, 46, 24, 732583, tzinfo=utc), max_length=2000),
            preserve_default=False,
        ),
    ]
