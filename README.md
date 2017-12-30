# Web scraper README

To fetch all the product URLs run the following command:
```
scrapy crawl product_urls -o ./data/product_urls.jl
```

To fetch the product's data:
```
scrapy crawl product_data -o ./data/products_data.jl
```