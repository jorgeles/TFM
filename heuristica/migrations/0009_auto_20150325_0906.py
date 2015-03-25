# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0008_auto_20150324_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='filatropo',
            new_name='filantropo',
        ),
    ]
