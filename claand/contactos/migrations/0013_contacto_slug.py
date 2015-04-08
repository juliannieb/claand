# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0012_auto_20150401_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
    ]
