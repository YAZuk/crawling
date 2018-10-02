# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    body = scrapy.Field()
    date = scrapy.Field()


class ItemProduct(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    # category_id = scrapy.Field()


class ItemCategory(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    # is_find = scrapy.Field()
