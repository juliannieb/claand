# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0006_auto_20150416_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='monto',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pago',
            name='monto',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venta',
            name='monto_total',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
    ]
