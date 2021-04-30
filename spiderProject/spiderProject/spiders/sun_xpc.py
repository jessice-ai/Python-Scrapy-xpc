

import scrapy
from scrapy import Request
from fake_useragent import UserAgent


class SunXpcSpider(scrapy.Spider):
    name = 'sun_xpc'
    allowed_domains = ['xinpianchang.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/type-/sort-like/duration_type-0/resolution_type-/page-1']

    headers = {
        'User-Agent': UserAgent().chrome
    }
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers)

    def parse(self, response):
        print(response.text)
        pass
