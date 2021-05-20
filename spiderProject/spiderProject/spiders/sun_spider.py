import scrapy

class SunSpiderSpider(scrapy.Spider):
    name = 'sun_spider'
    allowed_domains = ['chsi.com.cn']
    start_urls = ['https://yz.chsi.com.cn/sch/']


    def parse(self, response):
        # 返回内容 [<Selector xpath='//div[contains(@class,"yxk-table")]/table/tbody/tr/td[1]/a/text()' data='<a href="/sch/schoolInfo--schId-36787...'>,]
        # content = response.xpath('//div[contains(@class,"yxk-table")]/table/tbody/tr/td[1]/a/text()')
        # 返回内容 ['内容',]
        # extract 作用 把 [<Selector xpath='//div[contains(@class,"yxk-table")]/table/tbody/tr/td[1]/a/text()'>,] 转化为 ['内容',]
        content = response.xpath('//div[contains(@class,"yxk-table")]/table/tbody/tr/td[1]/a/text()').extract()
        for item in content:
            print(item.strip())  # 去掉前后空格
        # yield {
        #     'data':content
        # }