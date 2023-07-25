import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class MailSpider(CrawlSpider):
    
    name = "Ecrawler"
    allowed_domains = ["scrapebay.com"]
    start_urls = ["https://www.scrapebay.com"]
    
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        # filters email text from the source code of html file
        emails = re.findall(r'[\w\.]+@[\w\.]+', response.text)
        for email in emails:
            if 'bootstrap' not in email:
                yield{
                    'Email ' : email
                }