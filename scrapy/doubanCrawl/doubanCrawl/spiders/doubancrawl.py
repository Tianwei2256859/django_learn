# -*- coding: utf-8 -*-
import json
import re
import sys
sys.path.append('C:\Users\Administrator\Desktop\douban\doubanCrawl')
import scrapy
from scrapy.spiders import Spider
from doubanCrawl.items import DoubancrawlItem,DoubandetailcrawlItem
from scrapy.http import Request

class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'] 
    
    def parse(self, response):
        datas = json.loads(response.body)
        for data in datas:
        	ID = data['id']
        	title = data['title']
        	#cover_url = data['cover_url']
        	actors = '/'.join(data['actors'])
        	regions = '/'.join(data['regions'])
        	release_date = data['release_date'][:4]
        	types = '/'.join(data['types'])
        	score = data['score']
        	movielink = 'https://movie.douban.com/subject/%s/' % ID

        	movieitem = DoubancrawlItem(ID = ID, title = title,  actors = actors,
        			regions = regions, release_date = release_date, types = types, score = score)
        	yield movieitem
    		request = scrapy.Request(url = movielink, callback = self.parse_movie_detail)
    		request.meta['id'] = ID #电影id
    		request.meta['types'] = types #电影类型
    		request.meta['actors'] = actors #电影主演 
    		request.meta['regions'] = regions #制片国家/地区
    		request.meta['score'] = score #详情页面评分
    		yield request  	

        page_num = re.search(r'start=(\d+)', response.url).group(1)
        page_num = 'start=' + str(int(page_num)+20)
        next_url = re.sub(r'start=\d+', page_num, response.url)
        if next_url:
            yield scrapy.Request(url = next_url, callback = self.parse)

    def parse_movie_detail(self, response):
    	ID = response.meta['id'] #电影id
    	types = response.meta['types']#电影类型
    	actors = response.meta['actors']#电影主演 
    	regions = response.meta['regions'] #制片国家/地区
    	score = response.meta['score']#详情页面评分
    	big_title = response.xpath('.//*[@property="v:itemreviewed"]/text()').extract_first() #提取详情页面标题
    	image_url = (response.xpath('.//img[@rel="v:image"]/@src').extract_first()).replace('webp','jpg')#提取图片链接
    	runtime = response.xpath(".//*[@property='v:runtime']/text()").extract_first() # 片长
    	screewriter = '/'.join(response.xpath(".//*[@id='info']/span[2]/span[2]/a/text()").extract())# 编剧
    	director = response.xpath(".//*[@rel='v:directedBy']/text()").extract_first() #导演
        related_info = (response.xpath(".//*[@class='related-info']/div/span/text()").extract_first()).strip() # 剧情介绍
        if related_info :
        	related_info = related_info
        else:
        	related_info = response.xpath(".//*[@class='related-info']/div/span[2]/text()").extract_first()
        
        initialReleaseDate = '/'.join(response.xpath(".//*[@property='v:initialReleaseDate']/text()").extract())#上映日期

        moviedetailitem = DoubandetailcrawlItem(ID = ID, types = types, actors = actors, regions = regions,
        				score = score, big_title = big_title, dbimage_urls = image_url , runtime = runtime,
        				screewriter = screewriter, director = director, related_info = related_info,
        				initialReleaseDate = initialReleaseDate)
        yield moviedetailitem



        


