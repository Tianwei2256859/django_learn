# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20171101_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_info', models.CharField(max_length=255, null=True, verbose_name='\u6807\u9898\u4fe1\u606f:', blank=True)),
                ('release_date', models.CharField(max_length=255, null=True, verbose_name='\u4e0a\u6620\u5e74\u4efd:', blank=True)),
            ],
            options={
                'db_table': 'movie_info',
                'managed': True,
                'verbose_name_plural': '\u7535\u5f71\u4fe1\u606f',
            },
        ),
    ]
