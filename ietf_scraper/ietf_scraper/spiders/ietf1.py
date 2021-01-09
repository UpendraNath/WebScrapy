import scrapy


class Ietf1Spider(scrapy.Spider):
    name = 'ietf1'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/']

    def parse(self, response):
        pass
