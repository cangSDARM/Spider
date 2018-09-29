# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#爬虫数据结构
class MyscrapyItem(scrapy.Item):
	# define the fields for your item here like:
	# 固定写法, 所有数据都是字符串
	name = scrapy.Field()


#使用itemload加载item对象, 并追加字段.
#用在spider文件的parse中
from scrapy.contrib.loader import ItemLoader
class itemLoad():
	def parse(self, response):
		item = ItemLoader(item=MyscrapyItem(), response=response)
		item.add_xpath('name', '//div')		#使用xpath规则往MyscrapyItem中追加name字段
		xp = item.get_xpath('//div')		#使用xpath规则直接获取数据. 同response.xpath
		item.add_value('usr', xp)			#直接往item中追加usr字段
		
		yield item.load_item()				#yield item