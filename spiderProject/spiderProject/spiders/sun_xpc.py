import scrapy
from fake_useragent import UserAgent
from urllib.parse import urlparse
import json

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
            # print(url % item)
            request = response.follow(url % item,callback=self.parse_post,headers=self.headers,dont_filter=True)
            request.meta['sun_url'] = url % item  # 把值传递到回调函数中  self.parse_post
            yield request


    def parse_post(self,response):
        SunPost = {}
        SunPost['url'] = response.meta['sun_url'] #接收数据
        # .get() 与 .extract() 作用一样 从一个对象中得到列表[]
        sdrrTitle = response.xpath('//div[contains(@class,"title-wrap")]/h3/text()').extract()
        SunPost['titile'] = ""
        try:
            SunPost['titile'] = sdrrTitle[0]
        except Exception as result:
            print(result)

        mediaId = response.xpath('//a/@data-vid').get()

        if mediaId is not None:
            url = "https://mod-api.xinpianchang.com/mod/api/v2/media/" + mediaId + "?appKey=61a2f329348b3bf77&extend=userInfo,CuserStatus"

            # 注意:这里的Host变化
            # 原因: mod-api.xinpianchang.com 与 www.xinpianchang.com ping得到的IP不一样,顾需要重新设置host,否则接口调取失败
            headers = {
                'User-Agent': UserAgent().chrome,
                "Content-Type": "application/json;charset=utf-8",
                # Host 使用第一个网址中的全域名,如果手动写，注意 aaa.com 与 www.aaa.com 解析后的IP地址不同情况
                # Host 是 HTTP / 1.1 必须包含参数,作用:指定用户要访问的域名
                "Host": "%s:80" % urlparse(url).netloc,
            }
            #yield response.follow(url, callback=self.parse_video, headers=headers, dont_filter=True)
            request = scrapy.Request(url, callback=self.parse_video, headers=headers, dont_filter=True)
            request.meta['SunPost'] = SunPost #把值传递到回调函数中  self.parse_video
            yield request

        else:
            print('这个mediaId是None')


    def parse_video(self,response):

        #接受传递过来的值
        SunPost = response.meta['SunPost']
        dict = json.loads(response.text)
        video = dict['data']['resource']['progressive'][0]['url']
        SunPost['video'] = video
        print(SunPost)


