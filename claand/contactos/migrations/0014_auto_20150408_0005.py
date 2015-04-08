# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0013_contacto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='slug',
            field=models.SlugField(unique=True, null=True),
            preserve_default=True,
        ),
    ]
