import scrapy
from urllib.parse import urljoin
from spider.items import (
                            ItemCategory
                         )

SELECTOR_LIST_CATEGORIES = '//div[contains(@class,"yCmsContentSlot") ' \
                           'and ./div[contains(@class,"b-titleList--two")]]' \
                           '//a[contains(@class,"b-info__link--category") ' \
                           'or contains(@class,"b-account__item--label")]'


class SpiderKomusCategories(scrapy.Spider):
    """
        Проход по всем категориям
    """
    name = "spiderkomuscategories"
    start_urls = [
            'https://www.komus.ru/katalog/c/0/'
        ]
    visited_urls = []

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)
            for link in response.xpath(SELECTOR_LIST_CATEGORIES):

                item = ItemCategory()

                # ссылка на категорию
                try:
                    item['url'] = urljoin(response.url, link.xpath('@href').extract()[0])
                    self.logger.warning(item['url'])
                except IndexError:
                    item['url'] = ''
                # название категории
                try:
                    item['title'] = link.xpath('text()').extract()[0].replace('\xa0', '')
                    self.logger.warning(item['title'])
                except IndexError:
                    item['title'] = ''

                yield item
                yield response.follow(item['url'], callback=self.parse)
