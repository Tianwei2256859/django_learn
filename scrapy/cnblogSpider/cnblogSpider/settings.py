# -*- coding: utf-8 -*-

# Scrapy settings for cnblogSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cnblogSpider'

SPIDER_MODULES = ['cnblogSpider.spiders']
NEWSPIDER_MODULE = 'cnblogSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cnblogSpider (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3 # 设置延时2秒 
#RANDOMIZE_DOWNLOAD_DELAY=True #设置动态延迟
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16 #对单个网站进行并发请求的最大值
#CONCURRENT_REQUESTS_PER_IP=16 #对单个ip进行并发请求的最大值

# Disable cookies (enabled by default)
COOKIES_ENABLED=False # 禁用

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cnblogSpider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'cnblogSpider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'cnblogSpider.pipelines.CnblogspiderPipeline': 300, #激活 Item pipline
    'scrapy.pipelines.images.ImagesPipeline':400, #激活 Image pipline
} 
IMAGES_STORE = "D:\Scrapy\image" # 图片保存路径
IMAGES_URLS_FIELD = 'cimage_urls' #url所在item字段
IMAGES_RESULT_FIELD = 'cimages'  # 文件结果信息所在item字段
#IMAGES_EXPIRES = 30 # 过期时间
#IMAGES_THUMBS = {
	#'small': (50, 50),
	#'big': (270, 270),
#}
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True #启动自动限速扩展 4个AUTO
# The initial download delay 
#AUTOTHROTTLE_START_DELAY=5 #初始下载延时 默认为5秒 
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60 #设置在高延迟情况下最大的下载延迟
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False #启动debug模式

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
