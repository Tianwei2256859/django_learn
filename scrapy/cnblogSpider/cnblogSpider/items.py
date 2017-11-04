# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CnblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field() # 保存爬取到的数据 
    time=scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()
    cimage_urls=scrapy.Field()
    cimages=scrapy.Field()
