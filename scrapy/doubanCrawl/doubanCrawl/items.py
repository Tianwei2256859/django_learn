# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubancrawlItem(scrapy.Item):
    ID = scrapy.Field() #电影的id
    title = scrapy.Field() # 电影名称
    #cover_url = scrapy.Field() 
    actors = scrapy.Field() #主演
    regions = scrapy.Field() #制片国家/地区
    release_date = scrapy.Field() #上映时间
    types = scrapy.Field() #电影类型
    score = scrapy.Field() # 电影评分

class DoubandetailcrawlItem(scrapy.Item):
	ID = scrapy.Field()
	types = scrapy.Field()
	actors = scrapy.Field()
	regions = scrapy.Field()
	score = scrapy.Field()
	big_title = scrapy.Field()
	runtime = scrapy.Field()
	screewriter = scrapy.Field()
	director = scrapy.Field()
	initialReleaseDate = scrapy.Field()
	related_info = scrapy.Field()
	dbimage_urls = scrapy.Field()
	



