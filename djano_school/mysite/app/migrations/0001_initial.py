# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=30, verbose_name='\u73ed\u7ea7\u7f16\u53f7')),
                ('name', models.CharField(max_length=50, verbose_name='\u5b66\u6bb5')),
                ('grade', models.DateField(verbose_name='\u5b66\u5e74')),
                ('headmaster', models.CharField(max_length=10, verbose_name='\u73ed\u4e3b\u4efb')),
            ],
            options={
                'verbose_name_plural': '\u73ed\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=30, verbose_name='\u5b66\u6821id')),
                ('name', models.CharField(max_length=50, verbose_name='\u5b66\u6821\u540d\u79f0')),
                ('principal', models.CharField(max_length=30, verbose_name='\u6821\u957f')),
            ],
            options={
                'verbose_name_plural': '\u5b66\u6821',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=30, verbose_name='\u5b66\u751fid')),
                ('name', models.CharField(max_length=50, verbose_name='\u5b66\u751f\u540d\u5b57')),
                ('class_student', models.ForeignKey(verbose_name='\u5b66\u751f\u6240\u5728\u73ed\u7ea7', blank=True, to='app.Class', null=True)),
                ('student_school', models.ForeignKey(verbose_name='\u5b66\u751f\u6240\u5728\u5b66\u6821', blank=True, to='app.School', null=True)),
            ],
            options={
                'verbose_name_plural': '\u5b66\u751f',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=30, verbose_name='\u6559\u5e08id')),
                ('name', models.CharField(max_length=50, verbose_name='\u6559\u5e08\u540d\u5b57')),
                ('teach', models.CharField(max_length=50, verbose_name='\u4efb\u6559\u8bfe\u7a0b')),
                ('class_teacher', models.ManyToManyField(to='app.Class', null=True, verbose_name='\u6559\u5e08\u6240\u5728\u73ed\u7ea7', blank=True)),
                ('school_teacher', models.ForeignKey(verbose_name='\u6559\u5e08\u6240\u5728\u5b66\u6821', blank=True, to='app.School', null=True)),
            ],
            options={
                'verbose_name_plural': '\u6559\u5e08',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(verbose_name='\u4efb\u6559\u6559\u5e08', blank=True, to='app.Teacher', null=True),
        ),
        migrations.AddField(
            model_name='class',
            name='class_school',
            field=models.ForeignKey(verbose_name='\u73ed\u7ea7\u6240\u5728\u5b66\u6821', blank=True, to='app.School', null=True),
        ),
    ]
