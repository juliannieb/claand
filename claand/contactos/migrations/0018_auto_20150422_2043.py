# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0017_auto_20150422_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamada',
            name='descripcion',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recordatorio',
            name='descripcion',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
    ]
