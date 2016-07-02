# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fecha_perdido', models.DateField()),
                ('especie', models.CharField(max_length=25)),
                ('raza', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25)),
                ('sexo', models.CharField(max_length=1)),
                ('ultimo_lugar', models.TextField()),
                ('mas_informacion', models.TextField()),
                ('imagen', models.ImageField(upload_to='img-productos/')),
                ('creador', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
