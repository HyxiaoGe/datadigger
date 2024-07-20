import scrapy


class DatadiggerItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    imgUrl = scrapy.Field()
