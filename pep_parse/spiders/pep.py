import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import DOMAINS, NAME, START_URLS


class PepSpider(scrapy.Spider):
    name = NAME
    allowed_domains = DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        all_peps = response.css('a[href^="pep-"]')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css('h1.page-title::text').get().split()[1],
            'name': response.css('h1.page-title::text').get().split(' – ')[1],
            'status': response.css(
                'dt:contains("Status") + dd'
            ).css('abbr::text').get(),
        }
        yield PepParseItem(data)
