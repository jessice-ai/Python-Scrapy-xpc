# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from collections import defaultdict
from datetime import time

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy.exceptions import NotConfigured
from scrapy.utils.response import response_status_message
from twisted.internet import defer
from twisted.internet.error import DNSLookupError, TCPTimedOutError, ConnectionLost, ConnectError, ConnectionDone
from twisted.web._newclient import ResponseFailed


class SpiderprojectSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SpiderprojectDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

from urllib.parse import urlparse
from scrapy.exceptions import IgnoreRequest
#自定义中间件
class RandomProxyMiddlewate(object):

    sun_proxy = "" #代理属性 HTTP_PROXY 或  HTTPS_PROXY

    #第二部,初始化类属性
    def __init__(self,settings):

        # 这里涉及到了settings.py文件中的几个量
        # RETRY_ENABLED: 用于开启中间件，默认为TRUE
        # RETRY_TIMES: 重试次数, 默认为2
        # RETRY_HTTP_CODES: 遇到哪些返回状态码需要重试, 一个列表，默认为[500, 503, 504, 400, 408]
        # RETRY_PRIORITY_ADJUST：调整相对于原始请求的重试请求优先级，默认为-1

        if not settings.getbool('RETRY_ENABLED'):
            raise NotConfigured
        self.max_retry_times = settings.getint('RETRY_TIMES')
        self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
        self.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')

        self.PROXYS = settings.getlist('SUNPROXYS') #从设置中读取数据,并设置为类属性
        print('代理池中总共有 %s 个代理' % len(self.PROXYS))
        self.state = defaultdict(int)
        #self.max_failed = 3
        print('2、初始化类属性')

    #第一步,创建中间件对象
    @classmethod
    def from_crawler(cls,crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'): #判断是否启用代理,默认是启用的
            raise NotConfigured #如果settings中没有配置,则手动抛出异常
        print(' ' * 20)
        print(' ' * 20)
        print('1、创建中间件对象')
        return cls(crawler.settings)  #使用cls参数,执行 init 函数


    #第三步,为每一个request对象,设置一个IP代理
    def process_request(self,request,spider):
        # 这里的 random 选择 random 导入
        sx = random.choice(self.PROXYS)
        scheme = urlparse(sx).scheme
        netloc = urlparse(sx).netloc
        pre_proxy = ''
        if scheme == 'http':
            self.pre_proxy = 'HTTP_PROXY'
        elif scheme == 'https':
            self.pre_proxy = 'HTTPS_PROXY'

        if not request.meta.get(self.pre_proxy): #如果请求中没有proxy这个属性，则给设置一个随机的代理
            request.meta[self.pre_proxy] = netloc
            # print('3、为每一个request对象,设置一个随机IP代理')
            print('-' * 80)
            print(' ' * 80)
            print(' ' * 80)
            print("3、Request对象 request.meta[%s] = %s" % (self.pre_proxy,sx))
            print('-' * 80)
            print(' ' * 80)
        pass

    # 第四步、
    # 1、请求成功则调用该函数,请求失败不走该函数
    # 2、代理可用后,调用,(检查对方服务器是否禁用了这个代理)
    # 注意:process_response 与 process_exception 会执行一个
    def process_response(self,request,response,spider):
        # print(dir(request.meta))
        curl_proxy = request.meta.get(self.pre_proxy)
        #if response.status in (401,403):
        print('-' * 80)
        print(' ' * 80)
        print('4、请求成功, 继续验证,服务器返回码 代理 %s' % curl_proxy)
        #判断代理IP是否被对方服务器封禁
        if response.status != 200:
            #给相应的代理IP累计失败次数
            self.state[curl_proxy] += 1
            # print(self.state)
            print('5、服务器 -> 错误码 (%s) %s次 代理 %s' % (response.status, self.state[curl_proxy],curl_proxy))
            #当某个IP的失败次数累计到一定量
            if self.state[curl_proxy] >= self.max_retry_times:
                #可以认为该IP已经被对方服务器封禁,从代理池中删除该IP
                print('5、服务器 -> 错误码 (%s) ,拒绝IP 超%s次,已删除 代理 ' % (response.status, self.max_failed,curl_proxy))
                self.PROXYS.remove(curl_proxy)
                # 如果代理池中没有可用的代理,则抛出异常,请求就不再往下走了，到此为止
                if len(self.PROXYS) < 1:
                    raise IgnoreRequest
                del request.meta[self.pre_proxy]
                #注意
                # 1、返回request 作用: 将该请求,重新安排调度下载
                # 2、返回request重试时，在爬虫Spider里一定要用yield返回，否则不会重发request
                reason = response_status_message(response.status)
                # return self._retry(request, reason, spider) or response
                return request
            else:
                print('5、服务器 -> 错误码 (%s) 拒绝IP（%s） 次数 %s ' % (response.status,curl_proxy,self.state[curl_proxy]))
        else:
            print('5、服务器 -> 返回码 (%s) ' % response.status)
        return response
    # 第四步、
    # 1、请求失败则调用该函数，请求成功的话,不走该函数
    # 2、检测代理是否有异常
    # 注意:process_response 与 process_exception 会执行一个
    def process_exception(self,request,exception,spider):
        curl_proxy = request.meta.get(self.pre_proxy)
        # twisted.internet.error.ConnectionRefusedError 异常问题, twisted.internet.error.TimeoutError
        from twisted.internet.error import ConnectionRefusedError,TimeoutError,ConnectionDone
        from scrapy.spidermiddlewares import httperror
        # 有代理,且网络请求报错,则可认为该IP出现问题了,则从代理池中删除
        # 有代理,且出现该异常即是代理的问题 twisted.internet.error.ConnectionLost
        # defer 导入选择 twisted.internet.defer 导入
        # ConnectionLost 导入选择第一个
        EXCEPTIONS_TO_RETRY  = (defer.TimeoutError, TimeoutError, DNSLookupError,
                               ConnectionRefusedError, ConnectionDone, ConnectError,
                               ConnectionLost, TCPTimedOutError, ResponseFailed,
                               IOError, TunnelError)
        if curl_proxy and (isinstance(exception,EXCEPTIONS_TO_RETRY)):
            print('4、请求失败,异常:(%s) 代理 %s' % (exception,curl_proxy))
            print('-' * 80)
            if curl_proxy in self.PROXYS:
                self.PROXYS.remove(curl_proxy)
                print('代理池中剩余 %s 个 ' % len(self.PROXYS))
                #如果代理池中没有可用的代理,则抛出异常,请求就不再往下走了，到此为止
                if len(self.PROXYS) < 1:
                    raise IgnoreRequest
                del request.meta[self.pre_proxy]
                #这里要注释掉,如果代理有问题,则会自动切换其他代理,如果去掉注释不会自动重试,配合设置中的参数 RETRY_TIMES = 50 重试50次,直到成功,则停止
                # return request
                print('*'*100)



