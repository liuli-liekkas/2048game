import scrapy
from ..items import MovieSpiderItem
import re
import urllib

class movie87_spider(scrapy.Spider):
    name = "comedy"
    allowed_domains = ["www.87movie.com"]
    start_urls = ["http://www.87movie.com/tag/喜剧/"]

    def parse_info(self,response):
        movie_info = response.meta['movie_info']
        movie_info['name'] = response.xpath('//div[@class="white-div"]//h3/text()').extract()
        movie_info['pic'] = response.xpath('//div[@class="white-div"]//img/@src').extract()
        movie_info['content'] = response.xpath('//div[@class="white-div"]//div[@class="col-md-8"]/text()').extract()
        movie_info['download'] = response.xpath('//div[@id="down1"]/div[@class="panel-body"]/ul/li/a/@href').extract()
        return movie_info

    def parse_page(self, response):
        movies = response.xpath('//ul[@class="list-unstyled mlist"]/li//h4/a/@href').extract()
        url_host = 'http://' + response.url.split('/')[2]
        for i in movies:
            movie_info = MovieSpiderItem()
            yield scrapy.Request(url_host+i, meta={'movie_info': movie_info}, callback=self.parse_info)

    def parse(self, response):
        num_page = response.xpath('//ul[@class="pagination"]//li[last()]/a/@href').extract()
        number = 1
        if len(num_page) > 0:
            number = int(num_page[0].split('/')[-1].split('?')[0])
        for i in range(1, 3):
            if i > 4:
                return None
            yield scrapy.Request(response.url + str(i) + '?o=data', callback=self.parse_page)

class db_movie(scrapy.Spider):
    name = "douban_movie"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["http://movie.douban.com/later/shanghai"]

    def parse_info(self, response):
        movie_info = MovieSpiderItem()
        movie_info['title'] = response.xpath("//div[@id='content']/h1/span/text()").extract()
        movie_info['pic'] = response.xpath("//div[@id='mainpic']/a/img/@src").extract()
        movie_info['content'] = response.xpath("//div[@id='link-report']/span/text()").extract()
        movie_info['download'] = ""
        return movie_info

    def parse(self, response):
        movie_links = response.xpath("//div[@id='showing-soon']/div/div/h3/a/@href").extract()
        for i in movie_links:
            yield scrapy.Request(i, callback=self.parse_info)
