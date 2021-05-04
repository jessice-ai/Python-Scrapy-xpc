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
RETRY_TIMES = 50
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
REDIRECT_ENABLED = False
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
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
   'spiderProject.middlewares.RandomProxyMiddlewate': 749,
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

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

SUNPROXYS = [
    "http://136.243.211.104:80",
    "http://39.106.223.134:80",
    "http://39.102.32.69:3128",
    "http://167.71.5.83:3128",
    "http://60.191.11.241:3128",
    "http://74.143.245.221:80",
    "http://120.55.39.108:80",
    "http://47.113.111.149:80",
    "http://18.180.152.249:80",
    "http://103.136.202.242:80",
    "http://193.136.119.10:80",
    "http://8.129.126.49:80",
    "http://47.115.83.125:80",
    "http://134.3.255.8:8080",
    "http://138.68.60.8:8080",
    "http://118.179.223.130:80",
    "http://46.98.99.128:8080",
    "http://132.248.196.2:8080",
    "http://192.109.165.31:80",
    "http://152.169.106.145:8080",
    "http://223.82.106.253:3128",
    "http://47.115.15.170:80",
    "http://103.148.216.5:80",
    "http://123.231.175.42:8080",
    "http://114.112.127.18:80",
    "http://58.97.208.8:8080",
    "http://134.3.255.7:8080",
    "http://192.241.172.93:8081",
    "http://116.117.134.135:80",
    "http://176.9.119.170:8080",
    "http://103.46.233.23:83",
    "http://144.202.113.90:8080",
    "http://109.248.60.53:8081",
    "http://45.71.68.51:8080",
    "http://47.115.142.42:80",
    "http://157.90.4.42:8003",
    "http://183.88.226.50:8080",
    "http://47.115.116.5:80",
    "http://120.222.17.151:3128",
    "http://157.90.0.85:8080",
    "http://114.233.171.9:8044",
    "http://91.89.89.2:8080",
    "http://198.199.86.11:8080",
    "http://60.217.130.123:8060",
    "http://52.78.172.171:80",
    "http://218.253.39.60:8380",
    "http://149.172.255.10:3128",
    "http://72.23.14.208:80",
    "http://45.116.229.183:8080",
    "http://191.101.39.48:80",
    "http://46.5.252.61:8080",
    "http://101.109.83.194:8080",
    "http://183.88.128.8:8080",
    "http://194.79.63.134:8080",
    "http://187.243.255.174:8080",
    "http://103.78.255.66:8080",
    "http://181.39.22.150:8080",
    "http://213.216.67.190:8080",
    "http://46.5.252.62:8080",
    "http://190.109.169.41:53281",
    "http://31.131.67.14:8080",
    "http://201.91.82.155:3128",
    "http://47.112.237.208:80",
    "http://47.88.7.18:8088",
    "http://47.115.73.176:80",
    "http://154.16.202.22:3128",
    "http://157.90.0.82:8001",
    "http://78.47.16.54:80",
    "http://46.237.255.13:3128",
    "http://128.199.202.122:8080",
    "http://178.217.140.70:443",
    "http://95.111.128.43:37603",
    "http://139.162.78.109:8080",
    "http://47.57.188.208:80",
    "http://118.194.242.34:80",
    "http://51.81.82.175:2003",
    "http://191.96.42.80:8080",
    "http://109.193.195.3:8080",
    "http://47.112.152.228:80",
    "http://89.20.135.204:10000",
    "http://120.232.150.100:80",
    "http://191.96.71.118:3128",
    "http://121.230.91.21:8013",
    "http://46.5.252.55:8080",
    "http://109.193.195.4:8080",
    "http://134.209.29.120:8080",
    "http://190.120.249.247:999",
    "http://198.24.171.26:8099",
    "http://145.40.68.155:80",
    "http://195.140.226.244:8080",
    "http://46.237.255.10:3128",
    "http://136.232.209.70:47423",
    "http://114.233.169.251:8004",
    "http://47.112.154.149:80",
    "http://117.28.246.15:80",
    "http://39.101.221.247:9999",
    "http://101.51.139.179:84",
    "http://219.92.3.149:8080",
    "http://85.216.127.179:3128",
    "http://37.49.127.237:3128",
    "http://123.200.6.226:8080",
    "http://14.119.82.122:80",
    "http://125.141.117.19:80",
    "http://118.163.94.3:80",
    "http://181.98.174.28:80",
    "http://103.120.144.144:80",
    "http://103.141.105.157:80",
    "http://101.132.111.208:8082",
    "http://43.129.20.96:80",
    "http://137.59.155.14:80",
    "http://46.4.96.137:3128",
    "http://181.39.22.230:8080",
    "http://120.196.112.6:3128",
    "http://45.165.131.6:8080",
    "http://103.104.29.141:8080",
    "http://41.76.155.134:8080",
    "http://111.23.16.250:3128",
    "http://05.252.161.48:8080",
    "http://132.145.18.53:80",
    "http://45.177.111.57:999",
    "http://120.77.215.57:80",
    "http://31.173.94.93:43539",
    "http://161.35.70.249:3128",
    "http://88.198.50.103:3128",
    "http://37.49.127.226:8080",
    "http://217.8.51.200:3128",
    "http://118.194.242.156:80",
    "http://52.142.220.26:80",
    "http://1.179.144.41:8080",
    "http://183.89.30.43:8080",
    "http://154.16.63.16:3128",
    "http://178.212.54.137:8080",
    "http://47.95.205.25:8080",
    "http://176.9.75.42:3128",
    "http://47.116.76.219:80",
    "http://200.53.13.221:3128",
    "http://181.188.150.91:3128",
    "http://102.164.248.157:8080",
    "http://91.202.230.219:8080",
    "http://5.252.161.48:8080",
    "http://47.99.209.194:80",
    "http://82.212.62.29:8080",
    "http://189.206.105.164:80",
    "http://185.34.22.225:37879",
    "http://116.117.134.134:82",
    "http://106.51.252.229:80",
    "http://106.53.233.125:3128",
    "http://45.233.169.27:999",
    "http://139.59.1.14:3128",
    "http://150.109.32.166:80",
    "http://114.112.127.14:80",
    "http://102.129.249.120:3128",
    "http://47.103.130.208:38888",
    "http://203.202.245.58:80",
    "http://77.68.125.33:80",
    "http://75.119.144.28:80",
    "http://27.148.248.197:8091",
    "http://70.169.141.35:3128",
    "http://182.92.239.16:8080",
    "http://117.4.115.169:8080",
    "http://123.194.89.104:8380",
    "http://118.194.242.39:80",
    "http://217.8.51.199:8080",
    "http://120.232.150.110:80",
    "http://96.47.231.58:8020",
    "http://89.47.120.66:8080",
    "http://8.129.123.133:80",
    "http://102.141.210.93:53281",
    "http://46.223.255.13:3128",
    "http://60.255.151.82:80",
    "http://187.86.158.117:3128",
    "http://47.112.237.100:80",
    "http://124.48.218.245:80",
    "http://109.237.91.155:8080",
    "http://202.83.125.254:80",
    "http://46.36.74.60:8080",
    "http://159.203.61.169:3128",
    "http://102.91.6.10:8080",
    "http://82.212.62.24:8080",
    "http://209.97.150.167:8080",
    "http://202.61.51.204:3128",
    "http://192.109.165.37:80",
    "http://109.193.195.11:8080",
    "http://103.56.208.89:8080",
    "http://212.129.29.139:80",
    "http://88.198.24.108:3128",
    "http://103.42.195.70:53281",
    "http://85.105.139.53:8090",
    "http://35.172.135.29:80",
    "http://46.223.255.4:3128",
]