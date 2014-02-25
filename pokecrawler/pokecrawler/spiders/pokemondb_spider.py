from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
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
    	hxs = HtmlXPathSelector(response)

    	pokemon['name'] = hxs.select('//h1/text()')[0].extract()

    	types = hxs.select('//tr[th/text() = "Type"]/td/a/text()').extract()
    	if len(types) > 1:
    		pokemon['type1'] = types[0]
    		pokemon['type2'] = types[1]
    	else:
    		pokemon['type1'] = types[0]
    		pokemon['type2'] = "None"

    	pokemon['hp'] = hxs.select('//tr[th/text() = "HP"]/td/text()')[0].extract()
    	pokemon['attack'] = hxs.select('//tr[th/text() = "Attack"]/td/text()')[0].extract()
    	pokemon['defense'] = hxs.select('//tr[th/text() = "Defense"]/td/text()')[0].extract()
    	pokemon['spAttack'] = hxs.select('//tr[th/text() = "Sp. Atk"]/td/text()')[0].extract()
    	pokemon['spDefense'] = hxs.select('//tr[th/text() = "Sp. Def"]/td/text()')[0].extract()
    	pokemon['speed'] = hxs.select('//tr[th/text() = "Speed"]/td/text()')[0].extract()
    	pokemon['total'] = hxs.select('//tr[th/text() = "Total"]/td/b/text()')[0].extract()
    	return pokemon