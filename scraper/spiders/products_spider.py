import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = [
        'https://telekomunikace.heureka.cz/',
        'https://tv-video.heureka.cz/',
        'https://foto.heureka.cz/',
        'https://pocitace.heureka.cz/'
    ]

    def parse(self, response):
        # yield response.xpath('//li/h2/a/@href').extract()
        for url in response.xpath('//li/h2/a/@href'):
            yield {'url': url.extract()}
