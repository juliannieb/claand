# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0007_auto_20150320_0413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name_plural': 'Áreas', 'verbose_name': 'Área'},
        ),
        migrations.AlterModelOptions(
            name='calificacion',
            options={'verbose_name_plural': 'Calificaciones'},
        ),
        migrations.AlterModelOptions(
            name='numerotelefonico',
            options={'verbose_name_plural': 'Números Telefónicos', 'verbose_name': 'Número Telefónico'},
        ),
    ]
