# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0005_prueba'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prueba',
            old_name='apellidos',
            new_name='espiritu',
        ),
        migrations.AddField(
            model_name='prueba',
            name='filatropo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prueba',
            name='jugador',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prueba',
            name='logrador',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prueba',
            name='socializado',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
