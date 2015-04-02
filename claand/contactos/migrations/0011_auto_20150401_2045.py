# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0010_auto_20150401_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerotelefonico',
            name='numero',
            field=models.BigIntegerField(),
            preserve_default=True,
        ),
    ]
