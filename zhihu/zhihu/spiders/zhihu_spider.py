# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.selector import Selector
try:
	from scrapy.spider import Spider
except:
	from scrapy.spider import BaseSpider as Spider
# from scrapy.contrib.spiders import CrawlSpider, Rule

import scrapy
import re
from zhihu.items import zhihu_item


class zhihu_pider(Spider):
	name = "zhihu"
	allowed_domains = ["zhihu.com"]
	start_urls = [
		'http://news-at.zhihu.com/api/3/news/latest',
		'http://news.at.zhihu.com/api/3/news/before'
	]

	def parse(self, response):
		"""
		The lines below is a spider contract. For more info see:
		http://doc.scrapy.org/en/latest/topics/contracts.html
		@url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
		@scrapes name
		"""

		pattern = re.compile(r'[\S]*"date":"([\d]{8})[\S]*"stories":(\[.*\])[\S]*')
		pattern_item = re.compile(r'[\S]*"images":\["([\S]*)"\],"type":([\d]+),"id":([\d]*),"ga_prefix":"([\d]*)","title":"([\S]*)"\}')
		match = pattern.match(response.body)
		# match则组装items
		if match:
			match_item = pattern_item.findall(match.group(2))
			for i in match_item:
				item = zhihu_item()
				item['date'] = match.group(1)
				item['image'] = i[0]
				item['type'] = i[1]
				item['nid'] = i[2]
				item['ga_prefix'] = i[3]
				item['title'] = i[4]
				new_url = 'http://daily.zhihu.com/story/'+i[2]
				print 'new url------------->'+new_url
				yield scrapy.Request(new_url, meta={'item': item}, callback=self.parse_urls)

	def parse_urls(self, response):
		body = '';
		divs = response.xpath('//html//body//div[@class="content"]')
		for d in divs.xpath('.//p'):
			body = body + d.extract()
		body = body.replace('</p>', '\n')
		body = body.replace('<p>', '')
		item = response.meta['item']
		item['body'] = body
		return item