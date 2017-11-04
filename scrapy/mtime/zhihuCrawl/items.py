# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihucrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	MovieId = scrapy.Field() # 保存爬取到的数据 
	movieTitle = scrapy.Field()
	RatingFinal = scrapy.Field()
	ROtherFinal = scrapy.Field()
	RPictureFinal = scrapy.Field()
	RDirectorFinal = scrapy.Field()

	RStoryFinal = scrapy.Field() # 保存爬取到的数据 
	Usercount = scrapy.Field()
	AttitudeCount = scrapy.Field()
	TotalBoxOffice = scrapy.Field()
	TodayBoxOffice = scrapy.Field()
	Rank = scrapy.Field()
	ShowDays = scrapy.Field()
	isRelease = scrapy.Field()
