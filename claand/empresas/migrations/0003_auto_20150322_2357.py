# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20150322_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='id',
        ),
        migrations.AlterField(
            model_name='empresa',
            name='rfc',
            field=models.CharField(max_length=13, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
