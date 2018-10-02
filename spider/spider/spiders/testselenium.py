import scrapy
from selenium import webdriver

PATH_TO_DRIVER = r'/usr/bin/geckodriver'

SELECTOR_LIST_GROUPS_KOMUS = '//div[contains(@class,"b-facet__block") ' \
                             'and ./div[contains(@data-name,"categoryFullTextSearch")]]' \
                             '//div[contains(@class,"js-search--more__wrapper") and contains(@class,"facetValues") ' \
                             'and contains(@class,"js-listHide")]' \
                             '//label[contains(@class,"b-search__blockItem")]' \
                             '//span[@class="b-checkbox__label"]'

SELECTOR_BUTTON_MORE = '//div[contains(@class,"b-facet__block") ' \
                       'and ./div[contains(@data-name,"categoryFullTextSearch")]]' \
                       '//div[contains(@class,"js-search--more__wrapper")]' \
                       '//div[contains(@class,"b-search--more")]' \
                       '//span[contains(@class,"b-link")]'

# '//div[contains(@class,"b-search--more") and contains(@style,"")]'


SELECTOR_IS_CHECKED_GROUPS = '//div[contains(@class,"b-facet__block") ' \
                             'and ./div[contains(@data-name,"categoryFullTextSearch")]]' \
                             '//div[contains(@class,"js-search--more__wrapper")]' \
                             '//label[contains(@class,"b-search__blockItem")]' \
                             '//input[contains(@class,"b-checkbox__input")]'


SELECTOR_PANEL_GROUPS_KOMUS = '//div[contains(@class,"yCmsContentSlot") ' \
                              'and ./div[contains(@class,"b-titleList--two")] ' \
                              'and ./div[contains(@class,"clearfix")]]' \
                              '//a[@class="b-info__link--category"]'


class KomusSpider(scrapy.Spider):
    name = "komus_spider"
    allowed_domains = ['komus.ru']
    start_urls = [
                    'https://www.komus.ru/search?text=стол',
                    # 'https://www.komus.ru/search?text=ножницы',
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
            # block_search = self.driver.find_elements_by_xpath(SELECTOR_IS_CHECKED_GROUPS)
            button_more = self.driver.find_elements_by_xpath(SELECTOR_BUTTON_MORE)

            if button_more:
                button_more[0].click()
            self.logger.error(button_more)
            self.logger.error(dir(button_more[0]))
            self.logger.error(button_more[0].get_attribute("style"))
            if groups:
                groups[index].click()
                index += 1
                if index == len(groups):
                    break
            else:
                break

            # self.logger.warning("Selected->%s", block_search[0].is_selected())

        self.driver.close()

    # def parse(self, response):
    #     self.driver.get(response.url)
    #
    #     index = 0
    #     groups = self.driver.find_elements_by_xpath(
    #         SELECTOR_PANEL_GROUPS_KOMUS
    #     )
    #     self.logger.warning(groups)
    #     self.driver.close()
