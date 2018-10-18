# -*- coding: utf-8 -*-
import scrapy


class FinancialSpider(scrapy.Spider):
    name = 'financial'
    allowed_domains = ['reuters.com']
    def start_requests(self):
        urls = [
            'https://www.reuters.com/finance/stocks/financial-highlights/ACB.TO',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)



