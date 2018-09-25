import scrapy

class mySpider(scarpy.Spider):
	#爬虫名
	name = 'sprider01'
	#域
	allowd_domains = ["http://www.baidu.com/"]
	#开始爬虫路径
	start_urls = ("http://www.baidu.com/news",)
	
	#下载器下载完成后处理响应文件. 之前几乎不用做任何事
	def parse(self, response):
		html = response.body	#取html内容