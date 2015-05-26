# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0011_mitest_asginados'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mitest',
            old_name='asginados',
            new_name='asignados',
        ),
    ]
