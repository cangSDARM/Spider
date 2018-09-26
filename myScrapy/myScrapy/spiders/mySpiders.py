import scrapy
from myScrapy.items import MyscrapyItem	#����item�ļ�

class mySpider(scrapy.Spider):
	#������
	name = 'sprider01'
	#��
	allowd_domains = ["www.baidu.com/"]
	#��ʼ����·��
	start_urls = ("www.baidu.com/news",)
	
	#������������ɺ�����Ӧ�ļ�. ֮ǰ�����������κ���
	#���Request�ظ�������Request
	def parse(self, response):
		html = response.body	#ȡhtml����
		rawdata = response.xpath("//biv")	#scrapy�Դ�xpath
		rawdata0 = rawdata.xpath("./h3").extract()	#extract()��xpath����תΪ�ַ���
		rawdata1 = rawdata.css()	#css����
		rawdata2 = rawdata.re()		#����
		
		item = MyscrapyItem()
		item['name'] = rawdata	#MyscrapyItem��name�ֶ�
		
		#yield �������request��item, �򷵻ش�����Ϣ
		# request��÷�itemǰ
		
		#������Engine����url, ���趨�´δ�����
		# callback��������ָ��. parseֻ�ǵ�һ�ε��ñ��붨��
		# dont_filter�Ƿ����������
		yield scrapy.Request(url, callback = self.parse, dont_filter=True)	
		
		#��������
		yield item	#����Pipeline
		#return item	#������Pipeline, �������� scrapy crawl mySpider -o file.txt �洢���ļ���
		
#CrawlSpider. Spider������, ���̳л���������, ����Rule����url����
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
class myCrawlSpider(CrawlSpider):
	name = 'crawlSpider'
	allowd_domains = ['www.baidu.com']
	start_urls = ['http://www.baidu.com/news']
	
	page_lx = LinkExtractor(allow=("start=\d+"))	#ƥ������. allow��ʾƥ�����
	page_lxs = LinkExtractor(restrict_xpaths=("//div"))	#ʹ��xpathƥ������.
	
	#����ƥ��˳�����callback. ƥ�䵽�ظ��İ��ն���˳����õ�һ��
	rules = [
		# fllow�Ƿ����: ��ȡ����ҳ���Ƿ����ƥ�����
		# ���������������������.
		Rule(page_lx, callback='parseContent', follow=True)
	]
	
	#CrawlSpider����callback parse!
	# �ڲ�ʹ��parseʵ�����߼�, ���ǽ�����ʧЧ
	def parseContent(self, response):
		#����yield request. ��ΪRuleд����
		
		yield item