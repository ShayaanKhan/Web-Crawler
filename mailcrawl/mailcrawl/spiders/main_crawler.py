from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    
    name = "Ecrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse_item(self, response):
        yield {
            "title":        response.css(".product_main h1::text").get(),
            "price":        response.css(".price-color::text").get(),
            "availability": response.css(".availability::text")[1].get().replace("\n","").replace(" ",""),
        }

    rules=(
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catelogue", deny="category"), callback=parse_item)
    )