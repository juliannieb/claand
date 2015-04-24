# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0016_auto_20150415_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamada',
            name='descripcion',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recordatorio',
            name='descripcion',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
    ]
