# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0012_auto_20150520_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignados',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('propietario', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('seleccionados', models.CharField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
