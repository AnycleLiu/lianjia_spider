# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaPicSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    href = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

class LianJiaDealItem(scrapy.Item):
    '''
        链家成交记录列表数据模型
         {
                "bizcircle_id": 611100865,
                "community_id": 2411052382585,
                "house_code": "105101063640",
                "title": "鸿隆广场 2室2厅 49.46㎡",
                "new_title": "鸿隆广场 2室2厅",
                "kv_house_type": "sold",
                "frame_id": "2415252431081087",
                "blueprint_hall_num": 2,
                "blueprint_bedroom_num": 2,
                "area": 49.46,
                "price": 2490000,
                "price_hide": "2**",
                "desc_hide": "近30天内成交",
                "unit_price": 50344,
                "sign_date": "2017.10.28",
                "sign_timestamp": 1509158750,
                "sign_source": "链家成交",
                "orientation": "西北",
                "floor_state": "高楼层/31层",
                "building_finish_year": 2006,
                "decoration": "其他",
                "building_type": "塔楼",
                "require_login": 0
            }
    '''

    title = scrapy.Field() # 房源标题
    new_title = scrapy.Field() 
    area = scrapy.Field() #面积
    orientation = scrapy.Field() #朝向
    sign_date = scrapy.Field() # 成交日期
    unit_price = scrapy.Field() # 单价
    price = scrapy.Field() # 成交总价