# coding: utf-8

from __future__ import unicode_literals

import uuid
from django.db import models


class Movie(models.Model):
    id = models.CharField(verbose_name=u'电影id', primary_key=True, max_length=255, default=uuid.uuid4)
    title = models.CharField(verbose_name=u'标题:', max_length=255, blank=True, null=True, )
    #title = models.CharField(verbose_name=u'大标题:', max_length=255, blank=True, null=True)
    actors = models.TextField(verbose_name=u'主演:', blank=True, null=True)
    screenwriter = models.CharField(verbose_name=u'编剧:', max_length=255, blank=True, null=True)
    director = models.CharField(verbose_name=u'导演:', max_length=255, blank=True, null=True)
    runtime = models.CharField(verbose_name=u'片长:', max_length=255, blank=True, null=True)
    regions = models.CharField(verbose_name=u'制片国家/地区:', max_length=255, blank=True, null=True)
    types = models.CharField(verbose_name=u'类型:', max_length=255, blank=True, null=True)
    #release_date = models.CharField(verbose_name=u'上映年份:', max_length=255, blank=True, null=True)
    initialreleasedate = models.CharField(db_column='initialReleaseDate', max_length=255, blank=True, null=True, verbose_name = u'上映日期:')
    related_info = models.TextField(verbose_name=u'剧情简介:', blank=True, null=True)
    img = models.ImageField(verbose_name=u'首页图片:', max_length=255, blank=True, null=True, upload_to='img')
    score = models.CharField(verbose_name=u'评分:', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'movie'
        verbose_name_plural = u'电影'

    def __unicode__(self):
        return self.title

class Movie_info(models.Model):
    id = models.CharField(verbose_name=u'电影id', primary_key=True, max_length=255, default=uuid.uuid4)
    title_info = models.CharField(verbose_name=u'标题信息:', max_length=255, blank=True, null=True, )
    release_date = models.CharField(verbose_name=u'上映年份:', max_length=255, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'movie_info'
        verbose_name_plural = u'电影信息'

    def __unicode__(self):
        return self.title_info
