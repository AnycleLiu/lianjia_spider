#/usr/bin/python3
# -*- utf-8 -*-

import json
import scrapy
from .. items import LianJiaDealItem
from . utils.lianjia_util import LianJiaUtil

class LianJiaSpider(scrapy.Spider):
    '''
        链家成交房源成交列表
    '''
    name = 'lianjia_glc_deal_spider'
    total_rows = 0
    url = '/house/chengjiao/search'

    def __init__(self):
        self.lianjia_util = LianJiaUtil()

    def start_requests(self):
        payload = {
            'city_id': '440300',
            'community_id':'2411052382585',
            'limit_count': 20,
            'limit_offset': 0
        }
        
        rqs = self.lianjia_util.build_request(self.url, payload)

        yield scrapy.Request(rqs['url'],\
         cookies=rqs['cookies'], meta={'proxy': 'http://localhost:8888'}, headers= rqs['headers'])

    def parse(self, response):
        data = json.loads(response.body_as_unicode())['data']
        self.total_rows = self.total_rows + len(data['list'])

        for i in  self.parse_core(data):
            yield i 

        if data['has_more_data'] == 1:
            payload = {
                'city_id': '440300',
                'community_id':'2411052382585',
                'limit_count': 20,
                'limit_offset': self.total_rows
            }
            rqs = self.lianjia_util.build_request(self.url, payload)

            yield scrapy.Request(rqs['url'], cookies=rqs['cookies'], \
            meta={'proxy': 'http://localhost:8888'}, headers= rqs['headers'], callback=self.parse)
    
    def parse_core(self, data):
        for i in data['list']:
            item = LianJiaDealItem()
            
            item['title'] = i['title']
            item['new_title'] = i['new_title']
            item['area'] = i['area']
            item['orientation'] = i['orientation']
            item['sign_date'] = i['sign_date']
            item['unit_price'] = i['unit_price']
            item['price'] = i['price'] / 10000

            self.logger.info(item)
            yield item
        
