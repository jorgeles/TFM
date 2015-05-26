# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0017_auto_20150523_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('idTest', models.CharField(max_length=200)),
                ('respuestas', models.CharField(max_length=200000)),
                ('seleccionados', models.CharField(max_length=200000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='asignados',
            name='seleccionados',
            field=models.CharField(max_length=200000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mitest',
            name='seleccionados',
            field=models.CharField(max_length=200000),
            preserve_default=True,
        ),
    ]
