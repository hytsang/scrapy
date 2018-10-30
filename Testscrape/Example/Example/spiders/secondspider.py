#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 04:01:41 2018

@author: angeltang919
"""

import scrapy
import sys; print(sys.path)
from Example.items import NewItem

class SecondSpider(scrapy.Spider):
    name = "secondspider"
    allowed_domains = ['www.superdatascience.com']
    start_urls = ['https://www.superdatascience.com']
    
    def parse(self, response):
        item = NewItem()
        item['main_headline']=response.xpath('//span/text()').extract()
        item['headline']=response.xpath('//title/text()').extract()
        item['url']=response.url
        item['project']=self.settings.get('BOT_NAME')
        item['spider']=self.name
        
        return item

        