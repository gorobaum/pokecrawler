# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PokecrawlerItem(Item):
    name = Field()
    pokeType = Field()
    hp = Field()
    attack = Field()
    defense = Field()
    spAttack = Field()
    spDefense = Field()
    speed = Field()
    total = Field()
    pass
