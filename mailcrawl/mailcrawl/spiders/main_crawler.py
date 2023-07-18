from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    
    name = "Ecrawler"

    # test 1
    # Which website it crawls
    # allowed_domains = ["toscrape.com"]
    # start_urls = ["http://books.toscrape.com/"]

    # # What it looks for and returns
    # def parse_item(self, response):
    #     yield {
    #         #"title":          response.css(".product_main h1::text").get(),
    #         # "price":          response.css(".price_color::text").get(),
    #         # "availability":   response.css(".availability::text")[1].get().replace("\n","").replace(" ",""),
    #         #"title":            response.css(".col-xs-6 a::text").getall(),
    #         #"Price":            response.css(".price_color::text").getall(),
    #     }
    
    # # What domains its allowed to explore
    # rules=(
    #     #Rule(LinkExtractor(allow="catalogue/category")),
    #     Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    #     #Rule(LinkExtractor(allow="catalogue/category"), callback="parse_item"),
    # )

    #test 2
    allowed_domains = ["yellowpages.com"]
    start_urls = ["https://www.yellowpages.com/search?search_terms=automotive&geo_location_terms=New%20York%2C%20NY"]
    
    def parse_item(self, response):
        yield{
            "title":    response.css(".result h2::text").get()
        }

    # rules=(
    #     Rule(LinkExtractor()),
    # )