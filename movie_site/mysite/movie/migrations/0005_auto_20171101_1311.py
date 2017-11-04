# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20171101_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'managed': True, 'verbose_name_plural': '\u7535\u5f71'},
        ),
    ]
