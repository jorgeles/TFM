# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0015_asignados_idtest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('idTest', models.CharField(max_length=200)),
                ('respuestas', models.CharField(max_length=200000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
