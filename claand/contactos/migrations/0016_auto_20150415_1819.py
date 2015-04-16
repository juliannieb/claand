# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0015_auto_20150414_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='calificaciones',
        ),
        migrations.AddField(
            model_name='contacto',
            name='calificacion',
            field=models.ForeignKey(to='contactos.Calificacion', null=True),
            preserve_default=True,
        ),
    ]
