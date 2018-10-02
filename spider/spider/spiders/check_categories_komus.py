import scrapy
from selenium import webdriver
from spider.settings import (
                            SELECTOR_BUTTON_MORE,
                            SELECTOR_LIST_GROUPS_KOMUS,
                            PATH_TO_DRIVER, SELECTOR_PANEL_GROUPS_KOMUS
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
                    # 'https://www.komus.ru/search?text=пакеты',
                    # 'https://www.komus.ru/search?text=клей',
                ]

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER)

    def parse(self, response):
        self.driver.get(response.url)

        index = 0
        while True:
            # слева панель с чекбоксами найденных групп
            groups_check = self.driver.find_elements_by_xpath(SELECTOR_LIST_GROUPS_KOMUS)
            # кнопка "Показать еще" если есть в панели найденных групп
            button_more = self.driver.find_elements_by_xpath(SELECTOR_BUTTON_MORE)
            # если есть панель с категориями
            groups_list = self.driver.find_elements_by_xpath(SELECTOR_PANEL_GROUPS_KOMUS)

            if groups_check:
                if button_more:
                    button_more[0].click()
                groups_check[index].click()
                index += 1
                if index == len(groups_check):
                    break
            elif groups_list:
                # self.logger.warning(len(groups_list))
                self.logger.warning(groups_list)
                # self.logger.warning(groups_list[0].text)
                # self.logger.warning(groups_list[0].screenshot_as_png)
                # self.logger.warning(groups_list[0].tag_name)
                # self.logger.warning(dir(groups_list[0]))
                break
            else:
                break

        self.driver.close()
