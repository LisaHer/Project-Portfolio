#koop, huur

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FundaSpider(CrawlSpider):
    name = 'funda_test'
    allowed_domains = ['funda.nl']
    start_urls = []
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='http://www.funda.nl/koop/amsterdam/', headers={
            'User-Agent': self.user_agent
        })


    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@data-object-url-tracking='resultlist']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@rel='next']"), follow = True)
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield{
            'address': response.xpath("normalize-space(//span[@class='object-header__title']/text())").get(),
            'offered_since': response.xpath("normalize-space(//dt[.='Aangeboden sinds']/following-sibling::dd[1]/span[1]/text())").get()

        }
