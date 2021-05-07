import scrapy
from fake_useragent import UserAgent
from urllib.parse import urlparse
import json

cookies = dict(

)
class SunXpcSpider(scrapy.Spider):
    name = 'sun_xpc'
    allowed_domains = ['xinpianchang.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/type-/sort-like/duration_type-0/resolution_type-/page-1']

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
            yield scrapy.Request(url, callback=self.parse, headers=self.headers, dont_filter=True)

    def parse(self, response):

        list = response.xpath('//ul[@class="video-list"]/li/@data-articleid').extract()  # extract() 从一个对象中得到列表[]
        for item in list:
            url = 'https://www.xinpianchang.com/a%s?from=ArticleList'
            # print(url % item)
            request = response.follow(url % item, callback=self.parse_post, headers=self.headers, dont_filter=True)
            request.meta['sun_url'] = url % item  # 把值传递到回调函数中  self.parse_post
            #yield request #这里禁止掉,表示其他页面不跑,取消注释抓取所有页面里面的内容

        # 分页代码
        pages = response.xpath('//div[@class="page"]/a/@href').extract()
        for page in pages:
            print('https://www.xinpianchang.com%s' % page)

            # 这里没有添加 dont_filter=True ,因为链接中有重复的,不添加,可自动去重
            yield response.follow('https://www.xinpianchang.com%s' % page, callback=self.parse, headers=self.headers,cookies={'Authorization':'33CFA2358B6C9135C8B6C9462A8B6C9B6588B6C9DBF6A1DFC7DB'})

    def parse_post(self, response):

        SunPost = {'url': response.meta['sun_url']}
        # .get() 与 .extract() 作用一样 从一个对象中得到列表[]
        stderrTitle = response.xpath('//div[contains(@class,"title-wrap")]/h3/text()').extract()
        SunPost['title'] = ""
        try:
            SunPost['title'] = stderrTitle[0]
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
            # yield response.follow(url, callback=self.parse_video, headers=headers, dont_filter=True)
            request = scrapy.Request(url, callback=self.parse_video, headers=headers, dont_filter=True)
            request.meta['SunPost'] = SunPost  # 把值传递到回调函数中  self.parse_video
            yield request

        else:
            print('这个mediaId是None')

    def parse_video(self, response):

        # 接受传递过来的值
        SunPost = response.meta['SunPost']
        dicts = json.loads(response.text)
        video = dicts['data']['resource']['progressive'][0]['url']
        SunPost['video'] = video
        print(SunPost)
