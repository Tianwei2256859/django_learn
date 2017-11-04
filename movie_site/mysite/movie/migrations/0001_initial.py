# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=255, serialize=False, verbose_name='\u7535\u5f71id', primary_key=True)),
                ('info', models.CharField(max_length=255, null=True, verbose_name='\u6807\u9898\u4fe1\u606f:', blank=True)),
                ('actors', models.TextField(null=True, verbose_name='\u4e3b\u6f14:', blank=True)),
                ('screenwriter', models.CharField(max_length=255, null=True, verbose_name='\u7f16\u5267:', blank=True)),
                ('director', models.CharField(max_length=255, null=True, verbose_name='\u5bfc\u6f14:', blank=True)),
                ('runtime', models.CharField(max_length=255, null=True, verbose_name='\u7247\u957f:', blank=True)),
                ('regions', models.CharField(max_length=255, null=True, verbose_name='\u5236\u7247\u56fd\u5bb6/\u5730\u533a:', blank=True)),
                ('types', models.CharField(max_length=255, null=True, verbose_name='\u7c7b\u578b:', blank=True)),
                ('initialreleasedate', models.CharField(max_length=255, null=True, verbose_name='\u4e0a\u6620\u65e5\u671f:', db_column='initialReleaseDate', blank=True)),
                ('related_info', models.TextField(null=True, verbose_name='\u5267\u60c5\u7b80\u4ecb:', blank=True)),
                ('img', models.ImageField(max_length=255, upload_to='img', null=True, verbose_name='\u9996\u9875\u56fe\u7247:', blank=True)),
                ('score', models.CharField(max_length=255, null=True, verbose_name='\u8bc4\u5206:', blank=True)),
            ],
            options={
                'db_table': 'movie',
                'managed': True,
                'verbose_name_plural': '\u7535\u5f71',
            },
        ),
    ]
