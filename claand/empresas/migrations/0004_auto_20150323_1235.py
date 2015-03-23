# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_auto_20150322_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaTieneDireccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateField()),
                ('direccion', models.ForeignKey(to='empresas.Direccion')),
                ('empresa', models.ForeignKey(to='empresas.Empresa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='tiporedsocial',
            options={'verbose_name_plural': 'Tipo Redes Sociales'},
        ),
        migrations.AddField(
            model_name='empresa',
            name='direcciones',
            field=models.ManyToManyField(through='empresas.EmpresaTieneDireccion', to='empresas.Direccion'),
            preserve_default=True,
        ),
    ]
