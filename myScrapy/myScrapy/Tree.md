# Scrapy

### ProjectName
        |-  ProjectName             ȫ���߼�
		|		|-  __init__.py		ȫ�ֳ�ʼ��
		|		|-  items.py		���ݽṹ
		|		|-  middlewares.py	Spider Middlewares �� Downloader Middlewares
		|		|-  pipelines.py	���ݹܵ��ļ�
		|		|-  settings.py		ȫ�������ļ�
		|		|-	start.py		(�Լ���)�Զ�������
		|		|-  spiders			����Ŀ¼
		|				|-  __init__.py	�����ʼ��
		|
        |-  scrapy.cfg				ȫ�������ļ�

### ����
Spiders       : �����Engine URL��ַ, ���߸�����Responses, �ռ�Data
Middlewares   : �м��
Scrapy Engine : ����������ͨѶ, �Լ��źź����ݵĴ���
Scheduler     : ������. �������Request����, ����һ����ʽ���������黹��Engine. û��Request��ֹͣ����
Downloader    : ��������������ҳ, ����Responses����Engine
Item Piperline: ������Item, ������������ݵĺ��ڴ���


## ��ʼ��
* cd projectĿ¼
* scrapy startproject ProjectName	����project
* scrapy genspider py�ļ��� ?.com	scrapyģ��. ָ��������
* scrapy genspider -t crawl py�ļ��� ?.com	����CrawlSpiderģ��
* scrapy crawl crawlName			��ʼִ������ΪcrawlName������
* scrapy crawl crawlName -o fileName.txt ִ�в��洢��txt�ļ���