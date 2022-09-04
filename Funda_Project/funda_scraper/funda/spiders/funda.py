#koop, huur

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FundaSpider(CrawlSpider):
    name = 'funda'
    allowed_domains = ['funda.nl']
    start_urls = []
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='http://www.funda.nl/koop/heel-nederland/', headers={
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
            'address': response.xpath("//span[@class='object-header__title']/text()").get(),
            'postal_code': response.xpath("//span[@class='object-header__subtitle fd-color-dark-3']/text()").get(),
            'offered_since': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][1]/dd[3]/span/text()").get(),
            'asking-price': response.xpath("//strong[@class='object-header__price']/text()").get(), 
            'sqm_price': response.xpath("//dd[contains(@class, 'asking-price')]/text()").get(),
            'energy_label': response.xpath("//span[starts-with(@class, 'energielabel')]/text()").get(),
            'housing_type': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][2]/dd[1]/span/text()").get(),
            'build_year': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][2]/dd[3]/span/text()").get(),
            'surface': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][3]/dd[@class='object-kenmerken-group-list']/dl/dd[1]/span/text()").get(),
            'number_rooms': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][4]/dd[1]/span/text()").get(),
            'number_bathrooms': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][4]/dd[2]/span/text()").get(),
            'bathroom_facilities': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][4]/dd[3]/span/text()").get(),
            'total_floors': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][4]/dd[4]/span/text()").get(),
            'isolation': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][5]/dd[2]/span/text()").get(),
            'heating': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][5]/dd[3]/span/text()").get(),
            'warm_water': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][5]/dd[5]/span/text()").get(),
            'cv_ketel': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][5]/dd[5]/span/text()").get(),
            'internet': response.xpath("//div[@class='object-kenmerken-body']/dl[@class='object-kenmerken-list'][5]/dd[6]/span/text()").get(),
            'land_ownership': response.xpath("//dl[@class='object-kenmerken-list'][6]/dd[2]/dl/dd[2]/span/text()").get(),
            'erfpacht': response.xpath("//dl[@class='object-kenmerken-list'][6]/dd[2]/dl/dd[3]/span/text()").get(),
            'location': response.xpath("//dl[@class='object-kenmerken-list'][7]/dd[1]/span/text()").get(),
            'garden': response.xpath("//dl[@class='object-kenmerken-list'][7]/dd[2]/span/text()").get(),
            'garden_size': response.xpath("//dl[@class='object-kenmerken-list'][7]/dd[3]/span/text()").get(),
            'balcony_terrace': response.xpath("//dl[@class='object-kenmerken-list'][7]/dd[5]/span/text()").get(),
            'parking': response.xpath("//dl[@class='object-kenmerken-list'][9]/dd/span/text()").get(),
            'inhabitants_neighborhood': response.xpath("//ul[@class='list-none px-4 py-1 border-t border-light-2 border-solid']/li[1]/div[2]/text()").get(),
            'families_with_kids_perc': response.xpath("//ul[@class='list-none px-4 py-1 border-t border-light-2 border-solid']/li[2]/div[2]/text()").get(),
            'neighborhood_price_sqm': response.xpath("//ul[@class='list-none px-4 py-1 border-t border-light-2 border-solid']/li[3]/div[2]/text()").get(),
            'description': response.xpath("//div[@class='object-description-body']/text()").getall()


        }
