# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20150322_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
