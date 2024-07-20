from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.NineNewsSpider import NineNewsSpider

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())

    process.crawl(NineNewsSpider)

    process.start()
