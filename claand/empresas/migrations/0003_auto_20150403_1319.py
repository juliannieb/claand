# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20150322_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaTieneDireccion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('direccion', models.ForeignKey(to='empresas.Direccion')),
                ('empresa', models.ForeignKey(to='empresas.Empresa')),
            ],
            options={
                'verbose_name_plural': 'Empresa tiene direcciones',
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
            field=models.ManyToManyField(to='empresas.Direccion', through='empresas.EmpresaTieneDireccion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='municipio',
            name='nombre',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
