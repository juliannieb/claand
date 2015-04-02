# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0011_auto_20150401_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerotelefonico',
            name='contacto',
            field=models.ForeignKey(to='contactos.Contacto', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='numerotelefonico',
            name='empresa',
            field=models.ForeignKey(to='empresas.Empresa', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='numerotelefonico',
            name='vendedor',
            field=models.ForeignKey(to='principal.Vendedor', blank=True, null=True),
            preserve_default=True,
        ),
    ]
