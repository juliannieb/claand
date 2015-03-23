# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cotizacion',
            options={'verbose_name_plural': 'Cotizaciones', 'verbose_name': 'Cotización'},
        ),
    ]
