# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from spider.items import spiderItem


class Spider(CrawlSpider):
    name = "Spider"
    redis_key = 'Spider:start_urls'
    start_urls = ['http://www.imooc.com/course/list']
    for i in range(2,29):
        start_urls.append("http://www.imooc.com/course/list?page=%s" % str(i))

    def parse(self,response):
        # print response.body
        item = spiderItem()
        selector = Selector(response)
        Items = selector.xpath('//*[@class="course-one"]')
        for eachItem in Items:
            Title = eachItem.xpath('a/h5/span/text()').extract()
            text = eachItem.xpath('a/div[2]/p/text()').extract()
            num = eachItem.xpath('a/div[2]/span[2]/text()').extract()
            item['title'] = Title
            item['text'] = text
            item['num'] = num
            yield item
        #nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        #第10页是最后一页，没有下一页的链接
        #if nextLink:
        #    nextLink = nextLink[0]
            #yield Request(self.url + nextLink,callback=self.parse)

