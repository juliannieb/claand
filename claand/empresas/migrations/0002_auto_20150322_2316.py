# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direccion',
            options={'verbose_name_plural': 'Direcciones', 'verbose_name': 'Dirección'},
        ),
        migrations.AlterModelOptions(
            name='redsocial',
            options={'verbose_name_plural': 'Redes Sociales'},
        ),
    ]
