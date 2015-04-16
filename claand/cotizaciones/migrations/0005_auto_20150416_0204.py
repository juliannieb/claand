# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0004_auto_20150414_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name_plural': 'Ventas', 'verbose_name': 'Venta'},
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_creacion',
            field=models.DateField(editable=False, default=datetime.datetime(2015, 4, 16, 7, 3, 58, 310989, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_modificacion',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 7, 4, 7, 974803, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='monto_acumulado',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
