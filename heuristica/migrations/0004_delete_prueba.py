# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0003_usuario_disruptor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prueba',
        ),
    ]
