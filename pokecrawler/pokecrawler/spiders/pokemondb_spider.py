from scrapy.spider import Spider
from scrapy.selector import Selector

from pokecrawler.items import PokecrawlerItem

class PokemonDBSpider(Spider):
    name = "pokemondb"
    allowed_domains = ["pokemondb.net"]
    start_urls = [
        "http://pokemondb.net/pokedex/bulbasaur"
    ]

    def parse(self, response):
    	pokemon = PokecrawlerItem()
    	sel = Selector(response)
    	pokemon['name'] = sel.xpath('//h1/text()').extract()
    	return pokemon