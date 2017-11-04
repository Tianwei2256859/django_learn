# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='info',
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='\u6807\u9898:', blank=True),
        ),
    ]
