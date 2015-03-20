# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('contactos', '0005_auto_20150319_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pertenece',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fecha', models.DateField()),
                ('area', models.ForeignKey(to='contactos.Area')),
                ('contacto', models.ForeignKey(to='contactos.Contacto')),
                ('empresa', models.ForeignKey(to='empresas.Empresa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contacto',
            name='empresa',
            field=models.ManyToManyField(to='empresas.Empresa', through='contactos.Pertenece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numerotelefonico',
            name='contacto',
            field=models.ForeignKey(to='contactos.Contacto', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numerotelefonico',
            name='empresa',
            field=models.ForeignKey(to='empresas.Empresa', null=True),
            preserve_default=True,
        ),
    ]
