import scrapy


class ProductUrlsSpider(scrapy.Spider):
    name = "product_urls"
    start_urls = [
        'https://telekomunikace.heureka.cz/',
        'https://tv-video.heureka.cz/',
        'https://foto.heureka.cz/',
        'https://pocitace.heureka.cz/'
    ]

    def parse(self, response):
        # Check if there is a main section
        if response.xpath('//div/div/div/h2/text()').extract_first() == 'Hlavní sekce':
            # Select main sections from from start_urls
            for url in response.xpath('//li/h2/a/@href'):
                yield response.follow(url.extract(), callback=self.parse)
        else:
            # parse_section method is a generator hence can't be called directly
            for item in self.parse_section(response):
                yield item

    def parse_section(self, response):
        # Process the page of products
        for product_url in response.xpath('//div/h2/a/@href'):
            url = product_url.extract()
            # Possibly will require more robust (regex based) validation
            if url.endswith('/'):
                yield {'url': url}

        # Notify scrapy to process next page
        next_page = response.css('a.next::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_section)
