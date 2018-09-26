# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.utils.project import get_project_settings	#获取setting字段. (自己加字段用)
#from scrapy.pipelines.images import ImagePipeline	#处理图片的管道
#from scrapy.pipelines.images import MediaPipeline	#处理多媒体的管道

#数据存储管道
class MyscrapyPipeline(object):
	def __init__(self):
		pass
	
	#在spider开启时方法调用, 可选
	def open_spider(self, spider):
		pass
	
	#必须写
	def process_item(self, item, spider):
		getItem = get_project_settings().get("Items")	#获取setting文件字段
		return item
		
	#在spider关闭时方法调用, 可选
	def close_spider(self, sider):
		pass
		
#Image处理管道
class MyImagePipeline(ImagePipeline):
	def get_media_requests(self, item, info):
		image_url = item['url']		#自己确定的url
		yield scrapy.Request(image_url)
		
	def item_completed(self, result, item, info):
		image_path = [x['path'] for ok, x in result if ok]	#固定写法
		
		import os
		os.rename(STOREPATH + image_path[0], NAME)
		return item