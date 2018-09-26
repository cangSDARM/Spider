#自动化爬虫
from scrapy import cmdline

cmdline.execute('scrapy crawl myScrapy'.split())	#在命令行执行爬虫. 实现自动化