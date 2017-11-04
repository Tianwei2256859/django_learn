# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import urllib
import scrapy
import sys,os
sys.path.append('C:\Users\Administrator\Desktop\douban\doubanCrawl')
from doubanCrawl.items import DoubancrawlItem, DoubandetailcrawlItem
from scrapy.pipelines.images import ImagesPipeline
#from scrapy.utils.project import get_project_settings
class DoubancrawlPipeline(object):
	def __init__(self, mongo_url, mongo_db):
		self.mongo_url = mongo_url
		self.mongo_db = mongo_db

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			mongo_url = crawler.settings.get('MONGO_URL'), 
			mongo_db = crawler.settings.get('MONGO_DATABASE', 'douban')
		)

	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.mongo_url) #建立连接
		self.db = self.client[self.mongo_db]#定义数据库

	def close_spider(self, spider):
		self.client.close()#关闭客户端

	def process_item(self, item, spider):
		
		if isinstance(item,DoubancrawlItem):
			self.process_movielist_item(item)
		else:
			self.proess_moviedetail_item(item)
		return item

	def process_movielist_item(self,item):
		self.db.movieInfo.insert(dict(item))#插入数据到数据库

	def proess_moviedetail_item(self,item):
		item['related_info'] = item['related_info'].strip()
		self.db.moviedetail.insert(dict(item))
		img_url = item['dbimage_urls']
		num = item['ID']
		local = os.path.join('H:\Images', num + '.jpg')
		urllib.urlretrieve(img_url, local)





    


