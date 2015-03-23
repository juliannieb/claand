# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0008_auto_20150322_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='es_cliente',
            new_name='is_cliente',
        ),
        migrations.AddField(
            model_name='llamada',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 5, 57, 18, 240134, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nota',
            name='clasificacion',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recordatorio',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 5, 57, 28, 951897, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recordatorio',
            name='urgencia',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
