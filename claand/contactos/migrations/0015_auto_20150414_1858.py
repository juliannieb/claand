# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0014_auto_20150408_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerotelefonico',
            name='numero',
            field=models.BigIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='numerotelefonico',
            name='tipo_numero',
            field=models.ForeignKey(null=True, to='contactos.TipoNumeroTelefonico'),
            preserve_default=True,
        ),
    ]
