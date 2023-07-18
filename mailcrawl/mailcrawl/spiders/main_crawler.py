from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    
    name = "Ecrawler"
    # Which website it crawls
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    # What it looks for and returns
    def parse_item(self, response):
        yield {
            "title":response.css(".product_main h1::text").get(),
            "price":response.css(".price_color::text").get(),
            "availability":response.css(".availability::text")[1].get().replace("\n","").replace(" ",""),
        }
    
    # What domains its allowed to explore
    rules=(
        #Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    )