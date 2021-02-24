# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:32:49 2020

@author: kshub
"""

import scrapy 
class Dojospider(scrapy.Spider):
    name = "Dojo"
    
    start_urls = ['https://www.searchdonation.com//ngos/tamil-nadu/page/1/'
                  'https://www.searchdonation.com//ngos/tamil-nadu/page/2/'
                  'https://www.searchdonation.com//ngos/tamil-nadu/page/3/'
                  'https://www.searchdonation.com//ngos/tamil-nadu/page/4/']
    
    def parse(self, response):
        link = response.url.split('/')
        filename = 'Dojo-%s.text' %link
        with open (filename, 'wb') as f:
            f.write(response.body)