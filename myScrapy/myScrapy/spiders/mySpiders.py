import scrapy
from myScrapy.items import MyscrapyItem	#导入item文件

class mySpider(scrapy.Spider):
	#爬虫名
	name = 'sprider01'
	#域
	allowd_domains = ["www.baidu.com/"]
	#开始爬虫路径
	start_urls = ("www.baidu.com/news",)
	
	#下载器下载完成后处理响应文件. 之前几乎不用做任何事
	#如果Request重复就舍弃Request
	def parse(self, response):
		html = response.body	#取html内容
		rawdata = response.xpath("//biv")	#scrapy自带xpath
		rawdata0 = rawdata.xpath("./h3").extract()	#extract()将xpath对象转为字符串
		rawdata1 = rawdata.css()	#css规则
		rawdata2 = rawdata.re()		#正则
		
		item = MyscrapyItem()
		item['name'] = rawdata	#MyscrapyItem的name字段
		
		#yield 如果不是request或item, 则返回错误信息
		# request最好放item前
		
		#重新向Engine申请url, 并设定下次处理函数
		# callback可以随意指定. parse只是第一次调用必须定义
		# dont_filter是否忽略域限制
		yield scrapy.Request(url, callback = self.parse, dont_filter=True)	
		
		#返回数据
		yield item	#交给Pipeline
		#return item	#不交给Pipeline, 但可以用 scrapy crawl mySpider -o file.txt 存储到文件中
		
#CrawlSpider. Spider的子类, 除继承基础数据外, 还有Rule来简化url规则
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
class myCrawlSpider(CrawlSpider):
	name = 'crawlSpider'
	allowd_domains = ['www.baidu.com']
	start_urls = ['http://www.baidu.com/news']
	
	page_lx = LinkExtractor(allow=("start=\d+"))	#匹配连接. allow表示匹配规则
	page_lxs = LinkExtractor(restrict_xpaths=("//div"))	#使用xpath匹配连接.
	
	#根据匹配顺序调用callback. 匹配到重复的按照定义顺序调用第一个
	rules = [
		# fllow是否跟进: 获取到网页后是否继续匹配规则
		# 其它参数可以做规则过滤.
		Rule(page_lx, callback='parseContent', follow=True)
	]
	
	#CrawlSpider不能callback parse!
	# 内部使用parse实现其逻辑, 覆盖将运行失效
	def parseContent(self, response):
		#不用yield request. 因为Rule写好了
		
		yield item