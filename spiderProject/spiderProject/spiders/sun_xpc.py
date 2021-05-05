

import scrapy
from scrapy import Request
from fake_useragent import UserAgent


class SunXpcSpider(scrapy.Spider):
    name = 'sun_xpc'
    allowed_domains = ['xinpianchang.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/type-/sort-like/duration_type-0/resolution_type-/page-1']

    headers = {
        'User-Agent': UserAgent().chrome,
    }
    def start_requests(self):
        for url in self.start_urls:
            # 说明 dont_filter=True Scrapy内置了重复过滤功能,设置为True表示,不过滤重复请求
            yield scrapy.Request(url, headers=self.headers,dont_filter=True)

    def parse(self, response):
        list = response.xpath('//ul[@class="video-list"]/li/@data-articleid').extract() # extract() 从一个对象中得到列表[]
        for item in  list:
            url = 'https://www.xinpianchang.com/a%s?from=ArticleList'
            #yield response.follow()
            print(url % item)
            yield response.follow(url % item,self.parse_post)
        pass

    def parse_post(self,response):
        title = response.xpath('//h3[contains(@class,"title fs_26 fw_600 c_b_3 short")]/text()').extract()
        print(title)
