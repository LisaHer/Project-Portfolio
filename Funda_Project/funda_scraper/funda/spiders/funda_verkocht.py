#koop, huur

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FundaSpider(CrawlSpider):
    name = 'funda_verkocht'
    allowed_domains = ['funda.nl']
    start_urls = []
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.funda.nl/koop/amsterdam/verkocht/sorteer-afmelddatum-af/', headers={
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
            'postal_code': response.xpath("normalize-space(//span[@class='object-header__subtitle fd-color-dark-3']/text())").get(),
            'offered_since': response.xpath("normalize-space(//dt[.='Aangeboden sinds']/following-sibling::dd[1]/span[1]/text())").get(),
            'asking-price': response.xpath("normalize-space(//dt[.='Vraagprijs']/following-sibling::dd[1]/span[1]/text())").get(),
            'surface': response.xpath("normalize-space(//dt[.='Wonen']/following-sibling::dd[1]/span/text())").get(),
            'energy_label': response.xpath("normalize-space(//dt[.='Energielabel']/following-sibling::dd[1]/span[1]/text())").get(),
            'housing_type': response.xpath("normalize-space(//dt[.='Soort appartement']/following-sibling::dd[1]/span[1]/text())").get(),
            'build_year': response.xpath("normalize-space(//dt[.='Bouwjaar']/following-sibling::dd[1]/span[1]/text())").get(),
            'number_rooms': response.xpath("normalize-space(//dt[.='Aantal kamers']/following-sibling::dd[1]/span[1]/text())").get(),
            'number_bathrooms': response.xpath("normalize-space(//dt[.='Aantal badkamers']/following-sibling::dd[1]/span[1]/text())").get(),
            'bathroom_facilities': response.xpath("normalize-space(//dt[.='Badkamervoorzieningen']/following-sibling::dd[1]/span[1]/text())").get(),
            'total_floors': response.xpath("normalize-space(//dt[.='Aantal woonlagen']/following-sibling::dd[1]/span[1]/text())").get(),
            'isolation': response.xpath("normalize-space(//dt[.='Isolatie']/following-sibling::dd[1]/span[1]/text())").get(),
            'heating': response.xpath("normalize-space(//dt[.='Verwarming']/following-sibling::dd[1]/span[1]/text())").get(),
            'warm_water': response.xpath("normalize-space(//dt[.='Warm water']/following-sibling::dd[1]/span[1]/text())").get(),
            'cv_ketel': response.xpath("normalize-space(//dt[.='Cv-ketel']/following-sibling::dd[1]/span[1]/text())").get(),
            'land_ownership': response.xpath("normalize-space(//dt[.='Eigendomssituatie']/following-sibling::dd[1]/span[1]/text())").get(),
            'erfpacht': response.xpath("normalize-space(//dt[.='Lasten']/following-sibling::dd[1]/span[1]/text())").get(),
            'location': response.xpath("normalize-space(//dt[.='Ligging']/following-sibling::dd[1]/span[1]/text())").get(),
            'balcony_terrace': response.xpath("normalize-space(//dt[.='Balkon/dakterras']/following-sibling::dd[1]/span[1]/text())").get(),
            'parking': response.xpath("normalize-space(//dt[.='Soort parkeergelegenheid']/following-sibling::dd[1]/span[1]/text())").get(),
            'garden': response.xpath("normalize-space(//dt[.='Tuin']/following-sibling::dd[1]/span[1]/text())").get(),
            'inhabitants_neighborhood': response.xpath("normalize-space(//div[.='Inwoners']/following-sibling::div[1]//text())").get(),
            'families_with_kids_perc': response.xpath("normalize-space(//div[.='Gezin met kinderen']/following-sibling::div[1]//text())").get(),
            'neighborhood_price_sqm': response.xpath("normalize-space(//div[.='Gem. vraagprijs / m²']/following-sibling::div[1]//text())").get()

        }
