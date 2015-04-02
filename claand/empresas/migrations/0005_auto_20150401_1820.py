# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_auto_20150323_1235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresatienedireccion',
            options={'verbose_name_plural': 'Empresa tiene direcciones'},
        ),
        migrations.AlterField(
            model_name='municipio',
            name='nombre',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
