import scrapy
from urllib.parse import urljoin
from spider.items import (
                            ItemProduct
                        )

from selenium.webdriver.firefox import webdriver


PRODUCT_NAME_SELECTOR = '//h1[@class="b-productName"]/text()'
PRODUCT_PRICE_SELECTOR = '//span[@class="i-fs30 i-fwb"]/text()'
PRODUCT_NEXT_PAGES_SELECTOR = '//a[contains(@class, "b-pageNumber__item") and not(contains(@class, "active"))]/@href'
# PRODUCT_LIST_SELECTOR = '//div[@class="n-snippet-cell2 i-bem b-zone b-spy-visible shop-history ' \
#                         'b-spy-visible_js_inited b-zone_js_inited n-snippet-cell2_js_inited"]/@href'

PRODUCT_LIST_SELECTOR = '//a[contains(@class,"shop-history__link") and contains(@class,n-snippet-cell2__image)' \
                        'and contains(@class,"link")]/@href'

# 'n-snippet-cell2__image shop-history__link link i-bem link_js_inited'


class SpiderYandexMarket(scrapy.Spider):
    """
        Проход по всем товарам в конкретной категории
    """

    name = "spideryandexmarket"
    start_urls = [
            'https://market.yandex.ru/catalog/67114/',
        ]
    visited_urls = []

    def __init__(self, **kwargs):
        super(SpiderYandexMarket, self).__init__(**kwargs)
        for i in kwargs.values():
            self.start_urls.append(i)

    def parse(self, response):
        if response.url not in self.visited_urls:
            # посещенные страницы
            self.visited_urls.append(response.url)
            # проходим по товарам на одной странице
            # self.logger.warning(response.xpath(PRODUCT_LIST_SELECTOR))
            for link in response.xpath(PRODUCT_LIST_SELECTOR):
                url = urljoin(response.url, link.extract())
                self.logger.warning(url)
                # парсим товар
                # yield response.follow(url, callback=self.parse_product)

            # # находим ссылки на другие страницы с этим товаром
            # next_pages = response.xpath(PRODUCT_NEXT_PAGES_SELECTOR).extract()
            # next_page = next_pages[-1]
            #
            # next_page_url = urljoin(response.url+'/', next_page)
            # # идем по ссылке на следущую страницу
            # yield response.follow(next_page_url, callback=self.parse)

    def parse_product(self, response):
        item = ItemProduct()
        # название товара
        title = response.xpath(PRODUCT_NAME_SELECTOR).extract()
        try:
            item['title'] = title[0]
        except IndexError:
            item['title'] = ''

        # цена товара
        price = response.xpath(PRODUCT_PRICE_SELECTOR).extract()
        item['url'] = response.url

        try:
            # TODO здесь нечитаемые символы убраны и вместо запятых точка(малясь костыльно)
            item['price'] = float(price[0].replace('\xa0', '').replace(',', '.'))
        except ValueError:
            item['price'] = 0.0
        except IndexError:
            item['price'] = 0.0

        yield item
