# Scrapy settings for pokecrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pokecrawler'

SPIDER_MODULES = ['pokecrawler.spiders']
NEWSPIDER_MODULE = 'pokecrawler.spiders'
ITEM_PIPELINES = {
    'pokecrawler.pipelines.PokecrawlerPipeline': 100,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pokecrawler (+http://www.yourdomain.com)'
