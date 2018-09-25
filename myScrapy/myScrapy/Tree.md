# Scrapy

### ProjectName
        |-  ProjectName             全局逻辑
		|		|-  __init__.py		全局初始化
		|		|-  items.py		数据结构
		|		|-  middlewares.py
		|		|-  pipelines.py	数据管道文件
		|		|-  settings.py		全局设置文件
		|		|-  spiders			爬虫目录
		|				|-  __init__.py	爬虫初始化
		|		
		|
        |-  scrapy.cfg				全局配置文件

### 流程
Spiders       : 分配给Engine URL地址, 或者负责处理Responses, 收集Data
Middlewares   : 中间件
Scrapy Engine : 负责组件间的通讯, 以及信号和数据的传递
Scheduler     : 调度器. 负责接收Request请求, 并按一定方式排列整理后归还给Engine
Downloader    : 负责下载所有网页, 并将Responses交给Engine
Item Piperline: 负责处理Item, 进行爬虫后数据的后期处理


## 初始化
* cd project目录
* scrapy startproject ProjectName	创建project
* scrapy genspider py文件名 *.com	scrapy模板. 指定爬虫域
* scrapy crawl crawlName			开始执行名字为crawlName的爬虫