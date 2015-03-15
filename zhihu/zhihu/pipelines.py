# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from utils import db


class WriteMySQLPipeline(object):

	def __init__(self):
		# 初始化数据库链接串
		db.init('mysql', 'giraffeDB', 'localhost', '3306')

	def process_item(self, item, spider):
		url = 'http://daily.zhihu.com/story/'+item['nid']
		title = item['title'].decode('utf-8')
		body = item['body']
		u1 = dict(nid=item['nid'], ga_prefix=item['ga_prefix'], url=url, body=item['body'], image=item['image'], title=title, date=item['date'], time=time.localtime(time.time()))
		try:
			db.insert('scrapy_zhihu', **u1)
		except:
			# update('update user set email=?, passwd=? where id=?', 'michael@example.org', '654321', 1000)
			db.update('update scrapy_zhihu set url=?, title=?, body=?, time=? where nid=?', url, title, body, time.localtime(time.time()), item['nid'])
		return item

	def spider_closed(self, spider):
		self.file.close()