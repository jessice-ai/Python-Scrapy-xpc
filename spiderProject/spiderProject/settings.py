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
CONCURRENT_REQUESTS = 10
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
COOKIES_ENABLED = False

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
HTTPPROXY_ENABLED = True
RETRY_PRIORITY_ADJUST = 1
SUNPROXYS = [
    'http://74.143.245.221:80',
    'http://139.224.8.254:8080',
    'http://223.247.170.102:9999',
    'http://117.57.95.175:3256',
    'http://106.14.195.200:8080',
    'http://182.84.145.162:3256',
    'http://153.36.134.101:9999',
    'http://218.88.204.18:3256',
    'http://41.59.90.92:80',
    'http://153.36.134.248:9999',
    'http://54.254.142.254:80',
    'http://220.174.236.211:8091',
    'http://111.72.193.23:3256',
    'http://106.14.123.167:8080',
    'http://58.255.206.194:9999',
    'http://112.193.122.169:3256',
    'http://81.12.106.158:8080',
    'http://114.106.135.71:3256',
    'http://106.14.187.138:8080',
    'http://104.236.31.251:8080',
    'http://223.247.169.205:9999',
    'http://106.14.121.15:8080',
    'http://114.104.135.52:3256',
    'http://183.166.136.198:3256',
    'http://117.89.95.213:4216',
    'http://223.247.170.101:9999',
    'http://111.177.192.81:3256',
    'http://101.132.190.95:8080',
    'http://120.232.150.100:80',
    'http://144.217.101.245:3129',
    'http://52.78.172.171:80',
    'http://124.205.153.19:80',
    'http://175.165.228.248:9999',
    'http://13.212.196.74:80',
    'http://112.245.17.202:8080',
    'http://51.255.7.223:43567',
    'http://95.216.194.46:1080',
    'http://201.142.225.50:8080',
    'http://103.28.121.58:80',
    'http://115.203.123.101:3000',
    'http://8.133.191.41:8080',
    'http://183.166.139.154:9999',
    'http://52.142.220.26:80',
    'http://223.247.169.226:9999',
    'http://222.129.35.93:57114',
    'http://8.133.191.41:8081',
    'http://35.179.75.239:80',
    'http://8.133.191.41:8888',
    'http://111.177.192.74:3256',
    'http://223.247.170.53:9999',
    'http://123.171.42.114:3256',
    'http://114.233.171.16:8041',
    'http://118.194.242.165:80',
    'http://101.132.99.150:8080',
    'http://185.14.160.26:7890',
    'http://106.15.92.43:8080',
    'http://106.14.215.192:8080',
    'http://198.50.163.192:3129',
    'http://139.99.102.114:80',
    'http://101.132.134.134:8080',
    'http://117.95.198.154:23180',
    'http://180.111.110.36:4216',
    'http://219.92.3.149:8080',
    'http://49.85.189.168:8012',
    'http://3.6.251.241:80',
    'http://92.204.129.161:80',
    'http://27.191.60.185:3256',
    'http://106.14.222.68:8080',
    'http://223.247.170.93:9999',
    'http://101.132.124.122:8080',
    'http://78.30.225.227:8080',
    'http://114.104.135.45:3256',
    'http://223.247.170.82:9999',
    'http://120.43.97.55:4216',
    'http://54.255.192.244:80',
    'http://202.83.125.254:80',
    'http://121.206.217.12:3256',
    'http://132.248.196.2:8080',
    'http://106.14.220.213:8080',
    'http://117.28.246.15:80',
    'http://106.14.222.34:8080',
    'http://113.76.207.177:4216',
    'http://101.205.120.102:80',
    'http://27.155.222.145:57114',
    'http://23.251.138.105:8080',
    'http://62.201.210.134:8888',
    'http://221.226.193.71:4216',
    'http://102.164.252.176:8080',
]