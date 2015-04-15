# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0003_auto_20150322_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='is_pendiente',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
