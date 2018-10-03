# -*- coding: utf-8 -*-

# Scrapy settings for spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider'
SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'
DATABASE = {
                'drivername': 'postgres',
                'host': 'localhost',
                'port': '5432',
                'username': 'postgres',
                'password': '',
                'database': 'crawling'
            }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'spider.middlewares.SpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'spider.middlewares.SpiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'spider.pipelines.ProductPipeline': 300,
    # 'spider.pipelines.CategoryKomusPipeline': 800,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# FEED_EXPORT_ENCODING = 'utf-8'

PATH_TO_DRIVER = r'/usr/bin/geckodriver'

SELECTOR_LIST_GROUPS_KOMUS = '//div[contains(@class,"b-facet__block") ' \
                             'and ./div[contains(@data-name,"categoryFullTextSearch")]]' \
                             '//div[contains(@class,"js-search--more__wrapper") and contains(@class,"facetValues") ' \
                             'and contains(@class,"js-listHide")]' \
                             '//label[contains(@class,"b-search__blockItem")]' \
                             '//span[@class="b-checkbox__label"]'

SELECTOR_BUTTON_MORE_KOMUS = '//div[contains(@class,"b-facet__block") ' \
                       'and ./div[contains(@data-name,"categoryFullTextSearch")]]' \
                       '//div[contains(@class,"js-search--more__wrapper")]' \
                       '//div[contains(@class,"b-search--more")]' \
                       '//span[contains(@class,"b-link") and contains(text(),"Показать еще")]'


SELECTOR_IS_CHECKED_GROUPS = '//div[contains(@class,"b-facet__block") ' \
                             'and ./div[contains(@data-name,"categoryFullTextSearch")]]' \
                             '//div[contains(@class,"js-search--more__wrapper")]' \
                             '//label[contains(@class,"b-search__blockItem")]' \
                             '//input[contains(@class,"b-checkbox__input")]'


SELECTOR_PANEL_GROUPS_KOMUS = '//div[contains(@class,"yCmsContentSlot") ' \
                              'and ./div[contains(@class,"b-titleList--two")]]' \
                              '//a[contains(@class,"b-info__link--category") ' \
                              'or contains(@class,"b-account__item--label")]'


SELECTOR_TAGS_KOMUS = '//ul[contains(@class,"tags")]'

SELECTOR_PRODUCT_NAME_KOMUS = '//h1[@class="b-productName"]/text()'
SELECTOR_PRODUCT_PRICE_KOMUS = '//span[@class="i-fs30 i-fwb"]/text()'
SELECTOR_PRODUCT_NEXT_PAGES_KOMUS = '//a[contains(@class, "b-pageNumber__item") and not(contains(@class, "active"))]'
SELECTOR_PRODUCT_LIST_KOMUS = '//a[@class="b-productList__item__descr--title"]/@href'
