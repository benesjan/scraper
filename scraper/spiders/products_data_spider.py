import scrapy


class ProductDataSpider(scrapy.Spider):
    name = "product_data"

    def start_requests(self):
        with open('./data/product_urls.csv', 'r') as f:
            for row in f:
                if row != 'url\n':
                    yield scrapy.Request(url=row, callback=self.parse)

    def parse(self, response):
        # TODO: process the data
        pass
