# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0005_auto_20150416_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_creacion',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
