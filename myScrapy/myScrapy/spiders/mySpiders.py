import scrapy

class mySpider(scarpy.Spider):
	#������
	name = 'sprider01'
	#��
	allowd_domains = ["http://www.baidu.com/"]
	#��ʼ����·��
	start_urls = ("http://www.baidu.com/news",)
	
	#������������ɺ�����Ӧ�ļ�. ֮ǰ�����������κ���
	def parse(self, response):
		html = response.body	#ȡhtml����