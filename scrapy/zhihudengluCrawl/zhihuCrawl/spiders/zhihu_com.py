
# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

import time
from PIL import Image
import json
class MyspiderSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/#signin']

    def start_requests(self):
        t = str(int(time.time() * 1000))
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + '&type=login&lang=en'
        return [Request(captcha_url, callback=self.parser_captcha, meta={'cookiejar':1})]

    def parser_captcha(self, response):
        with open('captcha.jpg', 'wb') as f:
            f.write(response.body)
            f.close()
        im = Image.open('captcha.jpg')
        im.show()
        
        captcha = raw_input("input the captcha with quotation mark\n>")
        return Request(url='https://www.zhihu.com/', callback=self.login,meta={'captcha':captcha, 'cookiejar':response.meta['cookiejar']})
    
    def login(self,response):
        xsrf = response.xpath('//input[@name="_xsrf"]/@value').extract()[0]
        return [FormRequest('https://www.zhihu.com/login/email',
                method='POST',
                meta = {'cookiejar':response.meta['cookiejar']},
                formdata = {
                    'email':'791622643@qq.com',
                    'password':'Tian2256859',
                    '_xsrf':xsrf,
                    'captcha_type':'en',
                    'captcha':response.meta['captcha'],
                },

                callback = self.after_login,
        )]


    def after_login(self,response):

        json_file = json.loads(response.text)
        if json_file['r'] == 0:
            print('success....dengluchenggong')
            print response.meta
            return [Request(
            self.start_urls[0],
            meta={'cookiejar':response.meta['cookiejar']},
            callback = self.parse_user_info,
            dont_filter=True)]
        
        else:
           print('faild...denglushibai')

    def parse_user_info(self, response):
        user_image_usr = response.xpath("//img[@class='Avatar Avatar--large UserAvatar-inner']/@src").extract_first()
        print user_image_usr 



        


        
       