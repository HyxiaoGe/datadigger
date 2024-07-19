BOT_NAME = "datadigger"

SPIDER_MODULES = ["datadigger.spiders"]
NEWSPIDER_MODULE = "datadigger.spiders"


ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
