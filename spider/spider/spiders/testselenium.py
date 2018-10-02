import scrapy
from selenium import webdriver
from spider.settings import (
                            SELECTOR_BUTTON_MORE,
                            SELECTOR_LIST_GROUPS_KOMUS,
                            PATH_TO_DRIVER
                        )


class KomusSpider(scrapy.Spider):
    name = "komus_spider"
    allowed_domains = ['komus.ru']
    start_urls = [
                    # 'https://www.komus.ru/search?text=стол',
                    'https://www.komus.ru/search?text=ножницы',
                    # 'https://www.komus.ru/search?text=ручка синяя'
                    # 'https://www.komus.ru/search?text=стол стекляный',
                    # 'https://www.komus.ru/search?text=бумага',
                ]

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER)

    def parse(self, response):
        self.driver.get(response.url)

        index = 0
        while True:
            groups = self.driver.find_elements_by_xpath(
                SELECTOR_LIST_GROUPS_KOMUS
            )
            button_more = self.driver.find_elements_by_xpath(SELECTOR_BUTTON_MORE)

            if button_more:
                button_more[0].click()
            if groups:
                groups[index].click()
                index += 1
                if index == len(groups):
                    break
            else:
                break

        self.driver.close()
