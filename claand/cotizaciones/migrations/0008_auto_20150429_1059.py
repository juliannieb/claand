# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0007_auto_20150427_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_creacion',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
