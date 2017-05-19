import json
import scrapy
import logging
import datetime
from scrapebitcoin.items import ScrapebitcoinItem


logger = logging.getLogger(__name__)


class QuotesSpider(scrapy.Spider):
    name = "scrapebitcoin"
    bitcoin_address = [ '12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw',
                        '115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn',
                        '13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94',
                        '1QAc9S5EmycqjzzWDc1yiWzr9jJLC8sLiY',
                        '15zGqZCTcys6eCjDkE3DypCjXi6QWRV6V1']
    url = 'https://blockchain.info/address/%s'
    price_url = 'https://blockchain.info/tobtc?currency=USD&value=1'
    price = 0

    def start_requests(self):
        price_request = scrapy.Request(url=self.price_url, callback=self.parse_price)
        yield price_request

    def parse(self, response):
        items = ScrapebitcoinItem(bitcoin=response.meta['items']['bitcoin'])
        total_received = float(response.css('#total_received > font > span::attr(data-c)').extract_first()) / 100000000
        items['bitcoin'] = float(items['bitcoin']) + float(total_received)
        items['bitprice'] = float(response.meta['items']['bitprice'])
        items['money'] = items['bitcoin'] / items['bitprice']
        if self.bitcoin_address:
            address = self.bitcoin_address.pop()
            request = scrapy.Request(url=self.url % address, headers={'meta': {'bitcoin': items['bitcoin']}},callback=self.parse)
            request.meta['items'] = items
            yield  request
        else:
            logger.info('Total: ' + str(items['bitcoin']) + ' 比特币')
            logger.info('Total: '+ ('%.2f' % items['money']) + ' 美元')

    def parse_price(self, response):
        self.price = json.loads(response.body_as_unicode())
        items = ScrapebitcoinItem(bitcoin=0, bitprice=self.price, money=0)
        request = scrapy.Request(url=self.url % self.bitcoin_address.pop(), callback=self.parse)
        request.meta['items'] = items
        yield request
