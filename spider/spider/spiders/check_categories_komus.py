import scrapy
from selenium import webdriver
from spider.settings import (
                            SELECTOR_BUTTON_MORE,
                            SELECTOR_LIST_GROUPS_KOMUS,
                            PATH_TO_DRIVER, SELECTOR_PANEL_GROUPS_KOMUS, SELECTOR_TAGS_KOMUS
                        )

from urllib.parse import urljoin
from spider.items import (
                            ItemProduct
                        )

PRODUCT_NAME_SELECTOR = '//h1[@class="b-productName"]/text()'
PRODUCT_PRICE_SELECTOR = '//span[@class="i-fs30 i-fwb"]/text()'
PRODUCT_NEXT_PAGES_SELECTOR = '//a[contains(@class, "b-pageNumber__item") and not(contains(@class, "active"))]'
PRODUCT_LIST_SELECTOR = '//a[@class="b-productList__item__descr--title"]/@href'


class KomusSpider(scrapy.Spider):
    name = "komus_spider"
    allowed_domains = ['komus.ru']
    start_urls = [
                    # 'https://www.komus.ru/search?text=стол',
                    'https://www.komus.ru/search?text=ножницы',
                    # 'https://www.komus.ru/search?text=скрепки',
                    # 'https://www.komus.ru/search?text=ручка синяя'
                    # 'https://www.komus.ru/search?text=стол стекляный',
                    # 'https://www.komus.ru/search?text=бумага',
                    # 'https://www.komus.ru/search?text=пакеты',
                    # 'https://www.komus.ru/search?text=клей',
                    # 'https://www.komus.ru/search?text=ящик',
                ]

    visited_urls = []
    is_checks = True

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER)

    def parse(self, response):
        self.driver.get(response.url)

        index = 0
        while self.is_checks:
            # слева панель с чекбоксами найденных групп
            groups_check = self.driver.find_elements_by_xpath(SELECTOR_LIST_GROUPS_KOMUS)
            # кнопка "Показать еще" если есть в панели найденных групп
            button_more = self.driver.find_elements_by_xpath(SELECTOR_BUTTON_MORE)
            # если есть панель с категориями
            groups_list = self.driver.find_elements_by_xpath(SELECTOR_PANEL_GROUPS_KOMUS)
            # если есть панель с категориями
            tag_list = self.driver.find_elements_by_xpath(SELECTOR_TAGS_KOMUS)

            if groups_check:
                if button_more:
                    button_more[0].click()
                groups_check[index].click()
                index += 1
                if index == 3:
                    self.is_checks = False
                    break
            # elif groups_list:
            #     self.logger.warning(groups_list)
            #     break
            # elif tag_list:
            #     self.logger.warning(tag_list)
            #     break
            # else:
            #     break
            #
        # проходим по товарам на одной странице
        for link in response.xpath(PRODUCT_LIST_SELECTOR):
            url = urljoin(response.url, link.extract())
            # парсим товар
            yield response.follow(url, callback=self.parse_product)

        next_pages = self.driver.find_elements_by_xpath(PRODUCT_NEXT_PAGES_SELECTOR)
        next_page = next_pages[-1]
        next_page.click()
        yield response.follow(self.driver.current_url, callback=self.parse)
        # self.driver.close()


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


