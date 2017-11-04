# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20171101_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_info',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=255, serialize=False, verbose_name='\u7535\u5f71id', primary_key=True),
        ),
    ]
