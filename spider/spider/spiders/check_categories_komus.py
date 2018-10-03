import scrapy
from selenium import webdriver
from urllib.parse import urljoin
# from itertools import izip, cycle, tee
from spider.settings import (
                            SELECTOR_BUTTON_MORE_KOMUS,
                            SELECTOR_LIST_GROUPS_KOMUS,
                            PATH_TO_DRIVER,
                            SELECTOR_PANEL_GROUPS_KOMUS,
                            SELECTOR_TAGS_KOMUS,
                            SELECTOR_PRODUCT_NAME_KOMUS,
                            SELECTOR_PRODUCT_PRICE_KOMUS,
                            SELECTOR_PRODUCT_NEXT_PAGES_KOMUS,
                            SELECTOR_PRODUCT_LIST_KOMUS
                        )


from spider.items import (
                            ItemProduct
                        )


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

        if response.url not in self.visited_urls:
            self.driver.get(response.url)
            self.visited_urls.append(response.url)
            # index = 0
            # groups_check = self.driver.find_elements_by_xpath(SELECTOR_LIST_GROUPS_KOMUS)
            # button_more = self.driver.find_elements_by_xpath(SELECTOR_BUTTON_MORE_KOMUS)
            # groups_list = self.driver.find_elements_by_xpath(SELECTOR_PANEL_GROUPS_KOMUS)
            # tag_list = self.driver.find_elements_by_xpath(SELECTOR_TAGS_KOMUS)

            # if groups_check:
            #     if button_more:
            #         button_more[0].click()
            #     groups_check[index].click()

            for link in response.xpath(SELECTOR_PRODUCT_LIST_KOMUS):
                url = urljoin(response.url, link.extract())
                yield response.follow(url, callback=self.parse_product)

            next_pages = self.driver.find_elements_by_xpath(SELECTOR_PRODUCT_NEXT_PAGES_KOMUS)
            a = iter(next_pages)
            for i in a:
                if "active" in i.get_attribute("class"):
                    next_url = next(a)
                    url = next_url.get_attribute("href")
                    # next_url.click()
                    # yield response.follow(self.driver.current_url, callback=self.parse)
                    # next_url.click()
                    yield response.follow(url, callback=self.parse)

                    # break

            # self.driver.close()

    def parse_product(self, response):
        item = ItemProduct()
        # название товара
        title = response.xpath(SELECTOR_PRODUCT_NAME_KOMUS).extract()
        try:
            item['title'] = title[0]
        except IndexError:
            item['title'] = ''

        # цена товара
        price = response.xpath(SELECTOR_PRODUCT_PRICE_KOMUS).extract()
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


