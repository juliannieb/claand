# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0002_auto_20150322_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cotizacion',
            old_name='es_pendiente',
            new_name='is_pendiente',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='completada',
            new_name='is_completada',
        ),
        migrations.AddField(
            model_name='pago',
            name='monto',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
