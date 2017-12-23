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
        # Select main sections from from start_urls
        for url in response.xpath('//li/h2/a/@href'):
            yield response.follow(url.extract(), callback=self.parse_section)

    def parse_section(self, response):
        # Process the page of products
        for product_url in response.xpath('//div/h2/a/@href'):
            url = product_url.extract()
            # Possibly will require more robust (regex based) validation
            yield {'url': url, 'valid': (url.endswith('/') and url.count('/') == 4)}

        # Notify scrapy to process next page
        next_page = response.css('a.next::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_section)
