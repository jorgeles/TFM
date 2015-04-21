# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heuristica', '0002_auto_20150411_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('aventuras', models.CharField(max_length=200)),
                ('accion', models.CharField(max_length=200)),
                ('fps', models.CharField(max_length=200)),
                ('simulacion', models.CharField(max_length=200)),
                ('plataformas', models.CharField(max_length=200)),
                ('estrategia', models.CharField(max_length=200)),
                ('deporte', models.CharField(max_length=200)),
                ('motor', models.CharField(max_length=200)),
                ('rol', models.CharField(max_length=200)),
                ('sandbox', models.CharField(max_length=200)),
                ('party', models.CharField(max_length=200)),
                ('educativo', models.CharField(max_length=200)),
                ('musical', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
