import json
import re
import scrapy
from lianjia_pic_spider.items import LianjiaPicSpiderItem

class LianJiaSpider(scrapy.Spider):
    '''
        链家图片房源高清图片抓取
    '''
    name = 'lianjia_pic_spider'
    start_urls = [
       # 'https://m.lianjia.com/sz/ershoufang/105101003740.html',
        'https://m.lianjia.com/sz/chengjiao/105100902772.html'
        ]
    #image_urls = []

    def parse(self, response):
        self.logger.info("parse")
        data = response.xpath('//ul[contains(@class,"pic_lists")]/@data-info').extract()[0]
        imgs = json.loads(data)

        #self.logger.info(imgs)

        item = LianjiaPicSpiderItem()
        item['image_urls'] = [re.sub('\.\d+x\d+\.', '.1024x.', i['url']) for i in imgs]

        yield item
