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
                if row.startswith("http"):
                    yield scrapy.Request(url=row.strip(), callback=self.parse)

    def parse(self, response):
        # Load the dataLayer variable from script
        data = json.loads(response.xpath('//body/script/text()').extract_first().split('= [')[1].split('];')[0])

        request_url = 'https://www.heureka.cz/direct/vyvoj-cen/?id=' + data['product_id']
        request = scrapy.Request(url=request_url, callback=self.parse_prices)
        request.meta['product_id'] = data['product_id']
        request.meta['product_name'] = data['product_name']
        request.meta['product_brand'] = data['product_brand']
        request.meta['product_url'] = response.url

        return request

    def parse_prices(self, response):
        product = {
            'product_id': response.meta.get('product_id'),
            'product_name': response.meta.get('product_name'),
            'product_brand': response.meta.get('product_brand'),
            'product_url': response.meta.get('product_url')
        }

        body = str(response.body)

        for value in body.split('&\\r\\n&'):
            if value.startswith('values='):
                min_values = value[7:].split(',')
                product['min_values'] = list(map(float, min_values))
            elif value.startswith('values_2='):
                max_values = value[9:].split(',')
                product['max_values'] = list(map(float, max_values))
            elif value.startswith('x_labels='):
                product['labels'] = value[9:].split(',')

        yield product
