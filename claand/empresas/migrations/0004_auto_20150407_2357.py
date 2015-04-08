# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_auto_20150403_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='rfc',
            field=models.CharField(unique=True, max_length=13),
            preserve_default=True,
        ),
    ]
