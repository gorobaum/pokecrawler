from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from pokecrawler.items import PokecrawlerItem

class PokemonDBSpider(CrawlSpider):
	name = "pokemondb"
	allowed_domains = ["pokemondb.net"]
	start_urls = ["http://pokemondb.net/pokedex/bulbasaur"]

	rules = (Rule(SgmlLinkExtractor(allow=("http://pokemondb.net/pokedex/"), unique=True, restrict_xpaths=('body/article/nav/a'))
        , callback="parse_item", follow=True),
    )

	def parse_item(self,response): 
		pokemon = PokecrawlerItem()
		sel = Selector(response)
		pokemon['name'] = sel.xpath('//h1/text()')[0].extract()

		types = sel.xpath('//tr[th/text() = "Type"]/td/a/text()').extract()
		if len(types) > 1:
			pokemon['type1'] = types[0]
			pokemon['type2'] = types[1]
		else:
			pokemon['type1'] = types[0]
			pokemon['type2'] = "None"

		pokemon['hp'] = sel.xpath('//tr[th/text() = "HP"]/td/text()')[0].extract()
		pokemon['attack'] = sel.xpath('//tr[th/text() = "Attack"]/td/text()')[0].extract()
		pokemon['defense'] = sel.xpath('//tr[th/text() = "Defense"]/td/text()')[0].extract()
		pokemon['spAttack'] = sel.xpath('//tr[th/text() = "Sp. Atk"]/td/text()')[0].extract()
		pokemon['spDefense'] = sel.xpath('//tr[th/text() = "Sp. Def"]/td/text()')[0].extract()
		pokemon['speed'] = sel.xpath('//tr[th/text() = "Speed"]/td/text()')[0].extract()
		pokemon['total'] = sel.xpath('//tr[th/text() = "Total"]/td/b/text()')[0].extract()

		return pokemon