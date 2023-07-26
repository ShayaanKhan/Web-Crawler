import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class MailSpider(CrawlSpider):
    
    name = "Ecrawler"
    allowed_domains = ["infohindihub.in"]
    start_urls = ["https://www.infohindihub.in"]
    
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        # filters email text from the source code of html file
        emails = re.findall(r"[0-9A-Z^-~]+@[-!#-'*+/-9=?A-Z^-~]+\.[A-Za-z]+\.[A-Za-z]*", response.text)
        for email in emails:
            if 'bootstrap' not in email:
                yield{
                'Email ' : email
                }