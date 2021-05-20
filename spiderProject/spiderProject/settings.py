# Scrapy settings for spiderProject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spiderProject'

SPIDER_MODULES = ['spiderProject.spiders']
NEWSPIDER_MODULE = 'spiderProject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spiderProject (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 6
RETRY_ENABLED = True
RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]
REDIRECT_ENABLED = False
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spiderProject.middlewares.SpiderprojectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'spiderProject.middlewares.RandomProxyMiddlewate': 100,
}

DOWNLOAD_TIMEOUT = 2
LOG_LEVEL = 'INFO'
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'spiderProject.pipelines.SpiderprojectPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
AUTOTHROTTLE_ENABLED = True
# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPPROXY_ENABLED = False
RETRY_PRIORITY_ADJUST = 1
SUNPROXYS = [
   'http://103.148.216.5:80',
   'http://103.78.254.78:80',
   'http://14.225.11.126:8080',
   'http://103.28.121.58:80',
   'http://120.55.39.108:80',
   'http://194.150.255.142:80',
   'http://116.117.134.135:9999',
   'http://183.88.226.50:8080',
   'http://136.243.211.104:80',
   'http://116.73.14.16:8080',
   'http://141.226.18.206:8080',
   'http://14.119.82.122:80',
   'http://103.120.144.144:80',
   'http://45.184.103.113:999',
   'http://137.59.155.14:80',
   'http://101.132.111.208:8082',
   'http://8.210.155.56:80',
   'http://47.75.90.57:80',
   'http://120.77.215.57:80',
   'http://47.116.76.219:80',
   'http://58.240.52.114:80',
   'http://91.202.230.219:8080',
   'http://47.89.153.213:80',
   'http://202.83.125.254:80',
   'http://14.7.183.127:80',
   'http://101.133.216.135:80',
   'http://41.76.155.134:8080',
   'http://60.255.151.82:80',
   'http://58.176.147.14:80',
   'http://203.202.245.58:80',
   'http://202.61.51.204:3128',
   'http://103.51.103.22:80',
   'http://77.68.125.33:80',
   'http://75.119.144.28:80',
   'http://102.67.19.132:8080',
   'http://103.89.152.190:8080',
   'http://85.105.139.53:8090',
]