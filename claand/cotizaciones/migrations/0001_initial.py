# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0005_auto_20150319_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('monto', models.FloatField(default=0)),
                ('descripcion', models.TextField()),
                ('es_pendiente', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(editable=False)),
                ('fecha_modificacion', models.DateField()),
                ('contacto', models.ForeignKey(to='contactos.Contacto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(editable=False)),
                ('fecha_modificacion', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('monto_total', models.FloatField(default=0)),
                ('completada', models.BooleanField(default=False)),
                ('cotizacion', models.OneToOneField(to='cotizaciones.Cotizacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pago',
            name='venta',
            field=models.ForeignKey(to='cotizaciones.Venta'),
            preserve_default=True,
        ),
    ]
