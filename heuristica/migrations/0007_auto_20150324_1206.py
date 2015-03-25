# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0006_auto_20150324_1204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prueba',
            new_name='Perfil',
        ),
    ]
