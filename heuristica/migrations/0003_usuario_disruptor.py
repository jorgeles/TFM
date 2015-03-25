# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0002_auto_20150324_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='disruptor',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
