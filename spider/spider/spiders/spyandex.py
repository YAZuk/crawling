# -*- coding: utf-8 -*-
import scrapy


class SpyandexSpider(scrapy.Spider):
    name = 'spyandex'
    allowed_domains = ['www.market.yandex.ru']
    start_urls = [
                    'http://www.market.yandex.ru/search?text=стул',
                    'http://www.market.yandex.ru/search?text=карандаш',
                    'http://www.market.yandex.ru/search?text=ластик',
                    'http://www.market.yandex.ru/search?text=ручка синяя',
                    ]

    def parse(self, response):
        """ ищем блок-категории, к которым относится предмет поиска"""
        # SET_SELECTOR = '//li[@class="_2HihpwObsk"]'
        # SET_SELECTOR = '//div[@class="SMIUZQVy8Y"]//div[@class="_10qy3atIck"]'
        SET_SELECTOR = '//div[@class="SMIUZQVy8Y"]'
        categories = response.xpath(SET_SELECTOR)
        # print('+++++++++++++++%s' % response)
        # for i in categories[0]:
        self.logger.info(categories)
        self.logger.info(categories[0].xpath('//ul[@class="_2BLXswkhGO"]//li[@class="_2HihpwObsk"]//a//span/text()'))
