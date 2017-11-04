# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_info'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'managed': False, 'verbose_name_plural': '\u7535\u5f71'},
        ),
    ]
