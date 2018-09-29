#Scripy-Redis

##Example-Path: ./Scripy-Redis

### Scripy 不支持分布式架构, Scripy-Redis是为更方便实现分布式而提供的附加组件
* 支持爬虫暂停
* pip install scrapy-redis

### 修改或添加的组件
- Scheduler
- Duplication Filter
- Item Pipeline
- Base Spider

### 分布式
- master端: 只有一个, 不负责爬虫. 负责维护静态数据库和Redis; url指纹判断(去重); request的分配
- slaver端: 不止一个, 负责爬虫. 提交新的request和data给master

### 步骤
slaver: scrapy runspider myspider.py		直接加spider文件名
master: redis; lpush redis_key http://www.baidu.com
