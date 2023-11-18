# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class ForexPairItem(scrapy.Item):
    symbol = scrapy.Field()
    group = scrapy.Field()
    base = scrapy.Field()
    quote = scrapy.Field()
    pass


class TimeSeriesItem(scrapy.Item):
    symbol = scrapy.Field()
    datetime = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    close = scrapy.Field()
    pass
