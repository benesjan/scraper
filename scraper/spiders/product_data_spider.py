import json
import scrapy


class ProductDataSpider(scrapy.Spider):
    name = 'product_data'
    input_file = ''

    def __init__(self, input_file='', **kwargs):
        self.input_file = input_file
        super().__init__(**kwargs)

    def start_requests(self):
        with open(self.input_file, 'r') as f:
            for row in f:
                if row != 'url\n':
                    yield scrapy.Request(url=row.strip(), callback=self.parse)

    def parse(self, response):
        # Load the dataLayer variable from script
        data = json.loads(response.xpath('//body/script/text()').extract_first().split("= [")[1].split("];")[0])
        # print(data['product_brand'])
        # print(data['product_name'])
