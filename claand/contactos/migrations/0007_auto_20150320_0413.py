# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
        ('contactos', '0006_auto_20150320_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atiende',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fecha', models.DateField()),
                ('contacto', models.ForeignKey(to='contactos.Contacto')),
                ('vendedor', models.ForeignKey(to='principal.Vendedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contacto',
            name='vendedor',
            field=models.ManyToManyField(through='contactos.Atiende', to='principal.Vendedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numerotelefonico',
            name='vendedor',
            field=models.ForeignKey(to='principal.Vendedor', null=True),
            preserve_default=True,
        ),
    ]
