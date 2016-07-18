# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('code', models.PositiveSmallIntegerField(default=1000)),
                ('thing', models.CharField(max_length=100)),
                ('definition', models.TextField()),
                ('example', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('code', models.PositiveSmallIntegerField(default=1000)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
    ]
