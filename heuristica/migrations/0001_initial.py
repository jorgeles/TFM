# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('usuario', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('disruptor', models.CharField(max_length=200)),
                ('filantropo', models.CharField(max_length=200)),
                ('socializador', models.CharField(max_length=200)),
                ('jugador', models.CharField(max_length=200)),
                ('logrador', models.CharField(max_length=200)),
                ('espiritu', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
