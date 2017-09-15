# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaommItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    home_page = scrapy.Field()
    age = scrapy.Field()
    location = scrapy.Field()
    user_id = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
