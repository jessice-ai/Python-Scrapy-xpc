import scrapy


class SunPixabaySpider(scrapy.Spider):
    name = 'sun_pixabay'
    allowed_domains = ['pixabay.com']
    start_urls = ['http://pixabay.com/']

    def parse(self, response):
        pass
