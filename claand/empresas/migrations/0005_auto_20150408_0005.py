# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_auto_20150407_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='slug',
            field=models.SlugField(unique=True, null=True),
            preserve_default=True,
        ),
    ]
