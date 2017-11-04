# coding: utf-8
import scrapy
import sys
import re
import time
import json
from scrapy.selector import Selector

sys.path.append('D:\Scrapy\zhihuCrawl\zhihuCrawl')
from items import ZhihucrawlItem
class ZhihuSpider(scrapy.Spider):
	name='zhihu'
	allowed_domains = ['theater.mtime.com']
	start_urls = [
	    "http://theater.mtime.com/China_Beijing/"
	]

	def parse(self,response):
		pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)') 
		urls = pattern.findall(response.body) #获取电影地址
		for url in  list(set(urls)): #set去重复
			t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
			rank_url = 'http://service.library.mtime.com/Movie.api' \
				'?Ajax_CallBack=true' \
				'&Ajax_CallBackType=Mtime.Library.Services' \
				'&Ajax_CallBackMethod=GetMovieOverviewRating' \
				'&Ajax_CrossDomain=1' \
				'&Ajax_RequestUrl=%s' \
				'&t=%s' \
				'&Ajax_CallBackArgument0=%s'%(url[0], t, url[1])
			if rank_url: #获取电影信息的动态加载地址
				yield scrapy.Request(url = rank_url, callback=self.parse_json, dont_filter=True) #request的地址和allow_domain里面的冲突，从而被过滤掉。可以停用过滤功能

	def parse_json(self,response):
		pattern = re.compile(r'=(.*?);') 
		result = pattern.findall(response.body)[0] #获取电影的主信息json
		if result != None:
			value = json.loads(result)
			try:
				isRelease = value.get('value').get('isRelease')
			except Exception,e:
				print e
				return None

			if isRelease:
				if value.get('value').get('hotValue') == None: #已经上映的
					return self._parese_release(value)
				else:
					return self._parse_no_release(value, isRelease=2) # 马上上映的
			else:
				return self._parse_no_release(value) # 还有一点时间上映的

	def _parese_release(self, value):
		try:
			isRelease = 1
			movieRating = value.get('value').get('movieRating')  #电影评级
			boxOffice = value.get('value').get('boxOffice') #票房信息
			movieTitle = value.get('value').get('movieTitle') #电影标题

			RPictureFinal = movieRating.get('RPictureFinal') #画面评分
			RStoryFinal = movieRating.get('RStoryFinal')
			RDirectorFinal = movieRating.get('RDirectorFinal')
			ROtherFinal = movieRating.get('ROtherFinal')
			RatingFinal = movieRating.get('RatingFinal')

			MovieId = movieRating.get('MovieId')
			Usercount = movieRating.get('Usercount')
			AttitudeCount = movieRating.get('AttitudeCount')

			TotalBoxOffice = boxOffice.get('TotalBoxOffice')
			TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
			TodayBoxOffice = boxOffice.get('TodayBoxOffice')
			TodayBoxOfficeUnit = boxOffice.get('TodayBoxOfficeUnit')
			ShowDays = boxOffice.get('ShowDays')

			try:
				Rank = boxOffice.get('Rank')
			except Exception,e:
				Rank = 0

			item = ZhihucrawlItem(MovieId= MovieId,
								  movieTitle = movieTitle,
								  RatingFinal = RatingFinal,
								  ROtherFinal = ROtherFinal,
								  RPictureFinal = RPictureFinal,
								  RDirectorFinal = RDirectorFinal,
								  RStoryFinal = RStoryFinal,
								  Usercount = Usercount,
								  AttitudeCount = AttitudeCount,
								  TotalBoxOffice = TotalBoxOffice + TotalBoxOfficeUnit,
								  TodayBoxOffice = TodayBoxOffice + TodayBoxOfficeUnit,
								  Rank = Rank,
								  ShowDays = ShowDays,
								  isRelease = isRelease)
			yield item
		except Exception,e:
			return 

	def _parse_no_release(self, value, isRelease = 0):
		movieRating = value.get('value').get('movieRating')
		movieTitle =value.get('value').get('movieTitle')

		RPictureFinal = movieRating.get('RPictRStoryFinalureFinal') 
		RStoryFinal = movieRating.get('RStoryFinal')
		RDirectorFinal = movieRating.get('RDirectorFinal')
		ROtherFinal = movieRating.get('ROtherFinal')
		RatingFinal = movieRating.get('RatingFinal')

		MovieId = movieRating.get('MovieId')
		Usercount = movieRating.get('Usercount')
		AttitudeCount = movieRating.get('AttitudeCount')

		try:
			Rank = value.get('value').get('hotValue').get('Ranking')
		except Exception,e:
			Rank = 0

		item = ZhihucrawlItem(MovieId= MovieId,
							  movieTitle = movieTitle,
							  RatingFinal = RatingFinal,
							  ROtherFinal = ROtherFinal,
							  RPictureFinal = RPictureFinal,
							  RDirectorFinal = RDirectorFinal,
							  RStoryFinal = RStoryFinal,
							  Usercount = Usercount,
							  AttitudeCount = AttitudeCount,
							  TotalBoxOffice = u'无',
							  TodayBoxOffice = u'无',
							  Rank = Rank,
							  ShowDays = 0,
							  isRelease = isRelease)
		yield item















		
			
