# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0005_auto_20150408_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redsocial',
            name='link',
            field=models.URLField(null='True'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='redsocial',
            name='tipo_red_social',
            field=models.ForeignKey(to='empresas.TipoRedSocial', null=True),
            preserve_default=True,
        ),
    ]
