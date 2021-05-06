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
   'socks5://184.178.172.14:4145',
'socks5://35.208.14.218:1080',
'socks5://198.8.94.170:39074',
'socks5://98.178.72.8:4145',
'socks5://65.21.49.222:9266',
'socks5://165.227.177.113:20699',
'socks5://72.206.181.103:4145',
'socks5://192.111.130.5:17002',
'socks5://45.33.45.209:9050',
'socks5://141.98.134.2:1080',
'socks5://192.111.135.21:4145',
'socks5://167.172.123.221:9200',
'socks5://132.148.129.108:27500',
'socks5://184.179.216.130:4145',
'socks5://72.206.181.123:4145',
'socks5://45.55.236.186:61204',
'socks5://69.163.163.62:51139',
'socks5://102.129.249.120:1080',
'socks5://184.181.217.204:4145',
'socks5://192.111.139.165:19402',
'socks5://157.90.152.32:1080',
'socks5://192.111.129.150:4145',
'socks5://72.49.49.11:31034',
'socks5://72.221.232.155:4145',
'socks5://192.111.130.2:4145',
'socks5://72.210.252.134:46164',
'socks5://13.57.71.133:2080',
'socks5://70.166.167.36:4145',
'socks5://192.111.137.35:4145',
'socks5://138.68.60.8:1080',
'socks5://104.248.48.181:30588',
'socks5://167.160.188.211:1080',
'socks5://192.111.139.162:4145',
'socks5://138.68.6.227:9071',
'socks5://70.185.68.155:4145',
'socks5://192.252.215.5:16137',
'socks5://192.111.137.37:18762',
'socks5://192.252.211.197:14921',
'socks5://173.244.200.156:37093',
'socks5://184.185.2.244:4145',
'socks5://184.185.2.45:4145',
'socks5://72.223.168.67:4145',
'socks5://192.111.129.145:16894',
'socks5://98.162.96.41:4145',
'socks5://72.212.63.101:4145',
'socks5://72.221.196.145:4145',
'socks5://192.111.139.165:4145',
'socks5://110.43.136.72:1080',
'socks5://69.163.164.61:51139',
'socks5://69.163.167.133:62764',
'socks5://182.92.169.93:10080',
'socks5://69.163.160.61:62764',
'socks5://161.35.70.249:1080',
'socks5://159.65.69.186:9200',
'socks5://165.227.177.113:9659',
'socks5://192.252.209.155:14455',
'socks5://192.210.231.70:48545',
'socks5://69.163.163.173:62764',
'socks5://72.210.252.137:4145',
'socks5://69.163.162.253:51139',
'socks5://198.199.86.11:1080',
'socks5://180.111.110.36:4216',
'socks5://98.184.33.205:4145',
'socks5://159.89.133.34:9050',
'socks5://120.196.228.12:1080',
'socks5://72.195.114.169:4145',
'socks5://98.185.94.76:4145',
'socks5://173.212.201.250:33464',
'socks5://64.227.5.189:9369',
'socks5://184.178.172.18:15280',
'socks5://46.4.96.137:1080',
'socks5://69.163.163.59:51139',
'socks5://183.164.227.129:4216',
'socks5://69.163.160.115:62764',
'socks5://176.9.75.42:1080',
'socks5://183.236.164.121:1081',
'socks5://120.236.251.104:1081',
'socks5://115.238.101.42:9053',
'socks5://174.64.199.82:4145',
'socks5://217.8.51.206:1080',
'socks5://69.163.166.236:15026',
'socks5://117.29.95.19:4216',
'socks5://173.212.201.250:23686',
'socks5://176.9.160.118:22836',
'socks5://49.234.182.243:1080',
'socks5://46.4.156.212:18588',
'socks5://103.216.82.19:6667',
'socks5://183.166.132.182:3000',
'socks5://117.89.25.143:4216',
'socks5://213.136.89.190:13492',
'socks5://110.184.229.225:1080',
'socks5://88.198.24.108:1080',
'socks5://98.188.47.150:4145',
'socks5://118.113.66.191:1080',
'socks5://91.89.89.9:1080',
'socks5://178.162.202.44:2344',
'socks5://8.135.28.152:1080',
'socks5://8.210.163.246:50009',
'socks5://135.181.18.96:38322',
'socks5://167.71.5.83:1080',
'socks5://120.26.66.53:1080',
'socks5://43.224.10.48:6667',
'socks5://103.216.82.18:6667',
'socks5://119.23.248.1:1080',
'socks5://59.59.150.220:4216',
'socks5://213.136.89.190:9657',
'socks5://117.31.29.168:4216',
'socks5://154.16.202.22:1080',
'socks5://176.9.119.170:1080',
'socks5://166.62.85.224:54492',
'socks5://37.49.127.229:1080',
'socks5://119.101.115.251:7891',
'socks5://117.31.29.163:4216',
'socks5://163.53.209.8:6667',
'socks5://149.172.255.14:1080',
'socks5://103.216.82.22:6667',
'socks5://150.129.54.111:6667',
'socks5://134.3.255.10:1080',
'socks5://78.42.42.45:1080',
'socks5://113.121.243.227:57114',
'socks5://115.233.222.244:1080',
'socks5://88.198.50.103:1080',
'socks5://213.136.89.190:34843',
'socks5://103.241.227.110:6667',
'socks5://120.38.240.171:4216',
'socks5://91.198.137.31:3542',
'socks5://181.6.167.171:1080',
'socks5://186.126.220.29:1080',
'socks5://183.148.239.122:53127',
'socks5://117.71.148.183:53127',
'socks5://111.1.36.134:9053',
'socks5://186.126.43.95:1080',
'socks5://82.212.62.28:1080',
'socks5://120.196.228.73:1081',
'socks5://27.116.51.178:6667',
'socks5://103.21.163.81:6667',
'socks5://213.136.89.190:56844',
'socks5://91.89.89.11:1080',
'socks5://213.136.89.190:5136',
'socks5://186.126.70.34:1080',
'socks5://183.162.159.34:4216',
'socks5://72.217.216.239:4145',
'socks5://58.118.228.100:1080',
'socks5://117.174.160.105:1080',
'socks5://188.166.104.152:44924',
'socks5://37.49.127.226:1080',
'socks5://142.93.208.5:50273',
'socks5://165.22.220.151:33318',
'socks5://206.189.158.28:47419',
'socks5://222.129.39.90:57114',
'socks5://192.111.135.18:18301',
'socks5://27.116.51.186:6667',
'socks5://46.5.252.51:1080',
'socks5://217.8.51.201:1080',
'socks5://114.116.246.230:1080',
'socks5://188.166.28.109:21855',
'socks5://103.251.225.16:6667',
'socks5://95.217.132.133:3213',
'socks5://98.162.25.23:4145',
'socks5://95.217.132.133:3366',
'socks5://142.93.137.235:1429',
'socks5://206.189.158.28:7905',
'socks5://178.165.44.122:1080',
'socks5://194.5.192.220:1080',
'socks5://117.89.25.53:4216',
'socks5://46.101.56.138:27961',
'socks5://111.1.36.132:9053',
'socks5://181.3.171.124:1080',
'socks5://95.217.132.133:3004',
'socks5://188.166.104.152:43330',
'socks5://8.210.163.246:50006',
'socks5://103.241.227.106:6667',
'socks5://186.126.104.83:1080',
'socks5://181.7.197.96:1080',
'socks5://94.154.156.112:12333',
'socks5://31.25.243.40:9167',
'socks5://46.151.197.254:8080',
'socks5://206.189.158.28:28483',
'socks5://103.241.227.107:6667',
'socks5://206.189.158.28:7476',
'socks5://103.224.82.234:1080',
'socks5://134.209.29.120:1080',
'socks5://101.53.158.48:9051',
'socks5://181.102.96.242:1080',
'socks5://43.224.10.32:6667',
'socks5://181.102.102.195:1080',
'socks5://95.217.132.133:3100',
'socks5://31.128.248.1:1080',
'socks5://95.217.132.133:3493',
'socks5://5.252.161.48:1080',
'socks5://165.22.220.151:16927',
'socks5://193.187.173.126:41080',
'socks5://119.28.134.196:1080',
'socks5://159.203.61.169:1080',
'socks5://103.241.227.114:6667',
'socks5://181.3.36.242:1080',
'socks5://103.251.214.167:6667',
'socks5://88.202.177.242:1080',
'socks5://195.189.60.97:8080',
'socks5://222.129.34.171:57114',
'socks5://151.106.34.139:1080',
'socks5://31.7.232.178:1080',
'socks5://139.162.78.109:1080',
'socks5://181.6.148.45:1080',
'socks5://210.16.73.85:1080',
'socks5://69.163.166.143:51139',
'socks5://192.248.190.123:8004',
'socks5://43.224.10.26:6667',
'socks5://183.164.226.187:4216',
'socks5://213.251.238.186:9050',
'socks5://103.113.149.212:1080',
'socks5://103.145.253.87:5555',
'socks5://103.224.103.116:1080',
'socks5://103.85.232.20:1080',
'socks5://128.1.138.120:9999',
'socks5://114.230.122.104:38801',
'socks5://36.89.86.49:56845',
'socks5://125.135.221.94:54557',
'socks5://139.99.104.233:5279',
'socks5://188.166.104.152:6683',
'socks5://191.96.71.118:1080',
'socks5://113.160.188.21:1080',
'socks5://114.36.81.64:3128',
'socks5://194.5.178.150:3636',
'socks5://103.85.232.146:1080',
'socks5://128.199.202.122:1080',
'socks5://13.239.21.202:1080',
'socks5://195.144.21.185:1080',
'socks5://185.255.96.54:2000',
'socks5://111.1.36.135:9053',
'socks5://95.0.219.196:1082',
'socks5://113.190.59.40:1080',
'socks5://133.167.100.251:9050',
'socks5://118.113.66.170:1080',
'socks5://202.57.132.77:4145',
'socks5://43.224.10.25:6667',
'socks5://43.224.10.11:6667',
'socks5://119.28.82.156:8008',
'socks5://157.230.43.255:1080',
'socks5://181.102.30.24:1080',
'socks5://103.82.219.42:9154',
'socks5://31.25.243.40:9426',
'socks5://154.16.63.16:1080',
'socks5://185.221.237.189:1113',
'socks5://117.31.29.178:4216',
'socks5://46.5.252.56:1080',
'socks5://181.3.102.48:1080',
'socks5://139.59.1.14:1080',
'socks5://115.238.101.41:9053',
'socks5://124.193.142.210:1080',
'socks5://95.217.132.133:3333',
'socks5://186.126.170.124:1080',
'socks5://188.166.28.109:3467',
'socks5://31.128.248.2:1080',
'socks5://95.111.243.157:9050',
'socks5://31.25.243.40:9255',
'socks5://43.224.10.23:6667',
'socks5://181.101.113.120:1080',
'socks5://95.217.132.133:3175',
'socks5://181.6.33.88:1080',
'socks5://181.0.9.118:1080',
'socks5://103.240.161.101:6667',
'socks5://36.94.126.50:1080',
'socks5://181.129.7.202:6699',
]