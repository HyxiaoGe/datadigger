import scrapy

from datadigger.items import DatadiggerItem


class NineNewsSpider(scrapy.Spider):
    name = "9News"
    allowed_domains = ['9news.com.au']
    start_urls = ["https://www.9news.com.au/artificial-intelligence"]

    def parse(self, response):
        articles = response.css('div.feed__stories article.py.story-block')

        for article in articles:
            item = DatadiggerItem()
            item['title'] = article.css('h3.story__headline span.story__headline__text::text').get()
            item['url'] = article.css('h3.story__headline a::attr(href)').get()
            item['date'] = article.css('time.story__time::text').get()
            item['imgUrl'] = article.css('figure.story__media img::attr(src)').get()
            yield item
