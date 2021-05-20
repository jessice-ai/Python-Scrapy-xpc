import json
import os
from urllib.parse import urlparse

import requests
import scrapy
import self as self
from fake_useragent import UserAgent


class SunPixabaySpider(scrapy.Spider):
    name = 'sun_pixabay'
    allowed_domains = ['pixabay.com']
    keyworld = 'memorial day'
    start_urls = ["https://pixabay.com/api/?key=17946669-543fe6c4c313739ab33b63515&q="+keyworld+"&image_type=photo"]

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
        # print(response)

        res = json.loads(response.text)
        # 创建目录
        filedir = './images/'
        if not os.path.isdir(filedir):  # 判断目录是否存在
            os.mkdir(filedir)  # 创建目录

        for item in res["hits"]:

            item_data = urlparse(item["largeImageURL"])
            filename = item_data.path  # 图片的文件名(带后缀)
            url_data = item_data.scheme + '://' + item_data.netloc + filename  # 图片完整地址(远程图片)
            filepre = os.path.splitext(filename)[-1] #文件后缀名 如: .jpg
            tags_file = item["tags"]+", largeImageURL "+", "+self.keyworld+" "+filepre
            filepath = filedir+tags_file  # 本地的存储信息 ./images/xxxx.jpg

            px = item["webformatWidth"]*item["webformatHeight"]
            resp = requests.get(url_data)
            with open(filepath,'wb') as f:  # 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
                for chunk in resp.iter_content(1024):  # 依块的形式写入内存,每次写入最大1024
                    f.write(chunk)

            pass
        pass
