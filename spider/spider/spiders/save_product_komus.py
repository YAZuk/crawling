import scrapy
from urllib.parse import urljoin
from spider.items import (
                            ItemProduct
                        )

PRODUCT_NAME_SELECTOR = '//h1[@class="b-productName"]/text()'
PRODUCT_PRICE_SELECTOR = '//span[@class="i-fs30 i-fwb"]/text()'
PRODUCT_NEXT_PAGES_SELECTOR = '//a[contains(@class, "b-pageNumber__item") and not(contains(@class, "active"))]/@href'
PRODUCT_LIST_SELECTOR = '//a[@class="b-productList__item__descr--title"]/@href'


class SpiderKomus(scrapy.Spider):
    """
        Проход по всем товарам в конкретной категории
    """

    name = "spiderkomus"
    start_urls = [
            # 'https://komus.ru/katalog/kantstovary/kalkulyatory/kalkulyatory-nastolnye/c/442/',
            'https://www.komus.ru/katalog/kantstovary/steplery-i-skoby/steplery-do-15-listov/c/4176/',
            # 'https://www.komus.ru/katalog/pismennye-prinadlezhnosti/ruchki-klassa-lyuks/c/14950/'
        ]
    visited_urls = []

    def __init__(self, **kwargs):
        super(SpiderKomus, self).__init__(**kwargs)
        for i in kwargs.values():
            self.start_urls.append(i)

    def parse(self, response):
        if response.url not in self.visited_urls:
            # посещенные страницы
            self.visited_urls.append(response
                                     .url)
            # проходим по товарам на одной странице
            for link in response.xpath(PRODUCT_LIST_SELECTOR):
                url = urljoin(response.url, link.extract())

                # парсим товар
                yield response.follow(url, callback=self.parse_product)

            # находим ссылки на другие страницы с этим товаром
            next_pages = response.xpath(PRODUCT_NEXT_PAGES_SELECTOR).extract()
            next_page = next_pages[-1]

            next_page_url = urljoin(response.url+'/', next_page)
            # идем по ссылке на следущую страницу
            yield response.follow(next_page_url, callback=self.parse)

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

        # item['category_id'] = 1
        yield item
