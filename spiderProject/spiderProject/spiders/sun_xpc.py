import scrapy
from fake_useragent import UserAgent
from urllib.parse import urlparse

class SunXpcSpider(scrapy.Spider):
    name = 'sun_xpc'
    allowed_domains = ['xinpianchang.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/type-/sort-like/duration_type-0/resolution_type-/page-2']

    headers = {
        'User-Agent': UserAgent().chrome,
        "Content-Type": "application/json;charset=utf-8",
        # Host 使用第一个网址中的全域名,如果手动写，注意 aaa.com 与 www.aaa.com 解析后的IP地址不同情况
        # Host 是 HTTP / 1.1 必须包含参数,作用:指定用户要访问的域名
        "Host": "%s:80" % urlparse(start_urls[0]).netloc,
    }

    def start_requests(self):
        for url in self.start_urls:
            # 说明 dont_filter=True Scrapy内置了重复过滤功能,设置为True表示,不过滤重复请求
            yield scrapy.Request(url,callback=self.parse, headers=self.headers,dont_filter=True)

    def parse(self, response):

        list = response.xpath('//ul[@class="video-list"]/li/@data-articleid').extract() # extract() 从一个对象中得到列表[]
        for item in  list:
            url = 'https://www.xinpianchang.com/a%s?from=ArticleList'
            yield response.follow(url % item,self.parse_post,headers=self.headers,dont_filter=True)


    def parse_post(self,response):
        post = {}
        post['titile'] = response.xpath('//h3[contains(@class,"title fs_26 fw_600 c_b_3 short")]/text()').extract()
        # yield post
        print(post)