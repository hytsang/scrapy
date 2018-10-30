#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 01:06:24 2018

@author: angeltang919
"""

import scrapy

class FirstSpider(scrapy.Spider):
    name = "FirstSpider"
    
    def start_requests(self):
        urls = [
                'http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
                    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quote-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
###########################

#import scrapy
#
#class Firstspiderv2(scrapy.Spider):
#    name = "quotes"
#    start_urls = [
#        'http://quotes.toscrape.com/page/1/',
#        'http://quotes.toscrape.com/page/2/',
#    ]
#
#    def parse(self, response):
#        page = response.url.split("/")[-2]
#        filename = 'quotes-%s.html' % page
#        with open(filename, 'wb') as f:
#            f.write(response.body)
#        self.log('Saved file %s' % filename)
         
    