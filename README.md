# Web scraper README

To fetch all the product URLs run the following command:
```
scrapy crawl product_urls -o ./data/product_urls.jl
```
**WARNING**: some subsections are in multiple sections --> deduplication necessary

To fetch the product's data:
```
scrapy crawl product_data -a input_file=/path/to/start/urls -o ./data/products_data.jl
```