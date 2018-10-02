# -*- coding: utf-8 -*-
import scrapy
# import sys
# sys.path.insert(0, '..models')
# from ..models import db_connect


class SpykomusSpider(scrapy.Spider):
    name = 'spykomus'
    start_urls = [
            # 'http://komus.ru/search?text=ручка шариковая синяя',
            # 'http://komus.ru/search?text=карандаш',
            # 'http://komus.ru/search?text=стул',
            # 'http://komus.ru/search?text=стол',
            'http://komus.ru/search?text=калькулятор',
            # 'http://komus.ru/search?text=ластик',
            # 'http://komus.ru/search?text=степлер',
            # 'http://komus.ru/search?text=фломастер',
            # 'http://komus.ru/search?text=пакеты',
            # 'http://komus.ru/search?text=бумага',
            # 'http://komus.ru/search?text=тетрадь',
            # 'http://komus.ru/search?text=тетрадь в клетку',
            # 'http://komus.ru/search?text=бумага',
            # 'http://komus.ru/search?text=конверт',
            # 'http://komus.ru/search?text=acer swift 3',
            # 'http://komus.ru/search?text=skdfjnksjdnf',
        ]
    visited_urls = []
    host = 'www.komus.ru'

    def parse(self, response):
        """ ищем блок-категории, к которым относится предмет поиска"""
        selector_trademark = '//div[@data-name="Trademark"]'
        selector_group = '(//div[@data-name="categoryFullTextSearch"])'
        selector_category = '//div[@data-cms-content-slot-name="rightPanelSlot-categoryCatalogPage"]'
        selector_ = '//div[@class="b-titleList--two clearfix"]'

        if response.xpath(selector_group):
            selector_categories = '(//div[@class="facetValues js-listHide js-search--more__wrapper"])[1]'\
                                  '//label//span'
            # self.logger.debug("--------------Search categories->%s" % response.xpath(selector_categories))
            finder_categories = response.xpath(selector_categories)

            for cat in finder_categories:
                self.logger.debug('Group->%s' % cat.xpath('text()').extract())

        if response.xpath(selector_trademark):
            selector_categories = '(//div[@class="facetValues js-listHide js-search--more__wrapper"])[2]'\
                                  '//label//span/text()'
            self.logger.debug("--------------Trademark categories->%s" %
                              response.xpath(selector_categories))

        if response.xpath(selector_category) and response.xpath(selector_):

            links = response.xpath('//a[@class="b-info__link--category"]')
            for link in links:
                self.logger.debug('Categorie->%s %s' % (self.host +
                                                        link.xpath('@href').extract()[0],
                                                        link.xpath('text()').extract()))
                # self.logger.debug('Categorie->%s' % link.xpath('text()').extract())

            links = response.xpath('//a[@class="b-account__item--label"]')

            for link in links:
                self.logger.debug('Categorie->%s %s' % (self.host +
                                                        link.xpath('@href').extract()[0],
                                                        link.xpath('text()').extract()))
