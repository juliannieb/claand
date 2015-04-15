# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0006_auto_20150414_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redsocial',
            name='link',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
