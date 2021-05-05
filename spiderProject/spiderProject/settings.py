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
CONCURRENT_REQUESTS = 1
RETRY_ENABLED = True
RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
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
DOWNLOAD_TIMEOUT = 10
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
    "http://116.117.134.135:9999",
    "http://60.191.11.241:3128",
    "http://23.97.173.57:80",
    "http://60.191.11.249:3128",
    "http://103.148.216.5:80",
    "http://132.248.196.2:8080",
    "http://188.126.38.185:80",
    "http://47.75.90.57:80",
    "http://103.78.254.78:80",
    "http://118.179.223.130:80",
    "http://216.21.18.194:80",
    "http://136.243.211.104:80",
    "http://120.232.150.100:80",
    "http://193.149.225.72:80",
    "http://117.28.246.15:80",
    "http://183.88.226.50:8080",
    "http://8.210.71.64:3128",
    "http://194.150.255.142:80",
    "http://14.119.82.122:80",
    "http://37.135.121.157:80",
    "http://78.47.16.54:80",
    "http://103.120.144.144:80",
    "http://43.129.20.96:80",
    "http://137.59.155.14:80",
    "http://219.92.3.149:8080",
    "http://45.184.103.113:999",
    "http://120.196.112.6:3128",
    "http://89.20.48.118:8080",
    "http://197.210.107.74:80",
    "http://27.124.44.77:80",
    "http://52.142.220.26:80",
    "http://103.56.208.250:8080",
    "http://47.56.4.34:80",
    "http://51.158.178.209:8888",
    "http://177.200.206.167:8080",
    "http://14.225.11.126:8080",
    "http://189.206.105.163:80",
    "http://39.101.221.247:9999",
    "http://91.202.230.219:8080",
    "http://177.70.172.244:8080",
    "http://58.240.52.114:80",
    "http://201.91.82.155:3128",
    "http://47.103.130.208:38888",
    "http://47.115.32.249:80",
    "http://45.32.31.97:80",
    "http://14.7.183.127:80",
    "http://123.194.89.104:80",
    "http://120.232.150.110:80",
    "http://106.53.233.125:3128",
    "http://60.255.151.82:80",
    "http://35.172.135.29:80",
    "http://202.83.125.254:80",
    "https://200.6.136.94:8080",
    "https://58.97.212.58:8080",
    "https://60.191.11.241:3128",
    "http://75.119.144.28:80",
    "https://170.239.223.34:8080",
    "https://197.155.83.17:8080",
    "http://193.56.157.39:8080",
    "https://216.169.73.65:34679",
    "https://107.178.9.186:8080",
    "https://36.89.122.240:49784",
    "http://77.68.125.33:80",
    "https://45.167.125.129:9991",
    "https://122.144.6.5:3888",
    "https://116.73.14.16:8080",
    "http://200.93.199.141:80",
    "https://47.115.15.170:80",
    "https://45.184.103.113:999",
    "https://200.41.150.83:54958",
    "https://203.150.113.194:8080",
    "https://175.106.10.164:8089",
    "https://142.165.167.117:53281",
    "https://132.248.196.2:8080",
    "https://103.121.199.142:8080",
    "https://103.116.202.98:8080",
    "https://47.115.142.42:80",
    "https://34.74.224.9:80",
    "https://183.88.226.50:8080",
    "https://121.230.91.249:8040",
    "https://37.113.132.8:8080",
    "https://203.158.167.25:8080",
    "https://124.122.59.78:8080",
    "https://103.230.211.29:8080",
    "https://185.23.110.106:8080",
    "http://59.94.176.111:3128",
    "https://47.115.116.5:80",
    "https://180.183.10.80:8213",
    "https://179.124.31.233:8080",
    "https://185.136.162.4:8080",
    "https://202.69.45.22:8080",
    "https://14.225.11.126:8080",
    "https://165.16.46.215:8080",
    "https://103.206.254.170:65103",
    "https://41.71.9.103:8080",
    "https://94.45.4.102:80",
    "https://36.81.120.220:8080",
    "https://173.208.215.213:41080",
    "https://195.238.71.49:53281",
    "https://180.183.112.76:8213",
    "https://201.91.82.155:3128",
    "https://190.60.104.218:3128",
    "https://60.191.11.249:3128",
    "https://178.219.31.252:8080",
    "https://114.233.171.61:8091",
    "https://181.209.79.220:8080",
    "https://86.34.197.6:23500",
    "https://103.139.156.122:83",
    "https://168.196.115.202:50000",
    "https://187.49.83.153:8080",
    "http://202.61.51.204:3128",
    "https://103.148.232.63:8080",
    "https://14.207.121.15:8080",
    "https://62.213.14.166:8080",
    "https://103.11.106.27:8181",
    "https://47.112.154.149:80",
    "https://195.140.226.244:8080",
    "http://203.202.245.58:80",
    "https://183.88.99.52:8213",
    "https://39.101.221.247:9999",
    "https://103.35.135.2:83",
    "https://80.243.158.6:8080",
    "https://219.92.3.149:8080",
    "https://85.198.250.135:3128",
    "https://216.21.18.194:80",
    "https://202.57.55.242:45112",
    "https://187.188.181.112:1994",
    "https://101.132.111.208:8082",
    "https://120.196.112.6:3128",
    "https://83.242.123.248:8080",
    "https://119.28.155.202:9999",
    "https://177.45.80.164:8080",
    "https://170.0.143.28:8080",
    "https://49.85.189.77:8061",
    "https://183.89.78.48:8080",
    "https://45.173.4.244:999",
    "https://121.230.89.105:8028",
    "https://186.157.242.229:8080",
    "http://78.142.232.116:8080",
    "https://182.72.150.242:8080",
    "https://103.151.47.225:8080",
    "https://118.186.63.71:80",
    "https://103.106.114.134:8080",
    "https://186.10.80.122:53281",
    "https://154.72.73.218:8080",
    "https://175.100.103.132:55667",
    "https://176.110.173.130:8080",
    "https://160.119.192.254:8080",
    "https://110.232.74.55:8080",
    "https://178.172.208.244:32231",
    "https://77.238.79.111:8080",
    "https://124.158.167.172:8080",
    "https://37.143.22.34:8080",
    "https://47.103.130.208:38888",
    "https://177.1.26.130:8080",
    "https://79.120.177.106:8080",
    "https://8.129.123.133:80",
    "https://168.228.195.90:999",
    "https://78.142.232.116:8080",
    "https://146.122.203.58:80",
    "https://103.98.128.51:8080",
    "https://209.91.216.173:8080",
    "https://138.219.217.4:999",
    "https://200.223.48.250:8080",
    "https://47.112.237.100:80",
    "https://36.90.2.58:8080",
    "https://202.61.51.204:3128",
    "https://121.230.88.127:8019",
    "https://102.67.19.132:8080",
    "https://193.56.157.39:8080",
    "http://182.253.168.218:8080",
    "https://186.225.46.90:8080",
    "https://101.109.190.22:8080",
    "https://114.233.171.213:8017",
    "https://129.226.52.93:443",
    "https://59.94.176.111:3128",
    "https://129.205.160.233:60643",
    "https://103.35.132.18:83",
    "https://181.129.174.68:8080",
    "https://36.90.183.192:8181",
    "https://204.199.148.155:8080",
    "https://106.52.188.59:3128",
    "https://183.89.151.99:8080",
    "https://103.51.103.22:80",
    "https://80.211.179.30:3128",
    "https://129.204.12.131:8080",

]