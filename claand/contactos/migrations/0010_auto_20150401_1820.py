# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0009_auto_20150322_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atiende',
            options={'verbose_name_plural': 'Atienden'},
        ),
        migrations.AlterModelOptions(
            name='pertenece',
            options={'verbose_name_plural': 'Pertenecen'},
        ),
    ]
