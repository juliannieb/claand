# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0002_auto_20150319_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='correoElectronico',
            new_name='correo_electronico',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='esCliente',
            new_name='es_cliente',
        ),
        migrations.AddField(
            model_name='contacto',
            name='apellido',
            field=models.CharField(default='', max_length=35),
            preserve_default=False,
        ),
    ]
