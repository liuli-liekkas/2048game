import scrapy
from ..items import FirstSpiderItem

class tubagua_spider(scrapy.Spider):
    name = "pic_spider"
    allowed_domains = ["www.ivsky.com"]
    start_urls = ["http://www.ivsky.com/tupian/renwutupian/"]

    def parse(self,response):
        sspider = FirstSpiderItem()
        sspider['pic'] = response.xpath('//ul[@class="ali"]/li//img/@src').extract()
        return sspider