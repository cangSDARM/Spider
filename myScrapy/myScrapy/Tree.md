# Scrapy

### ProjectName
        |-  ProjectName             ȫ���߼�
		|		|-  __init__.py		ȫ�ֳ�ʼ��
		|		|-  items.py		���ݽṹ
		|		|-  middlewares.py
		|		|-  pipelines.py	���ݹܵ��ļ�
		|		|-  settings.py		ȫ�������ļ�
		|		|-  spiders			����Ŀ¼
		|				|-  __init__.py	�����ʼ��
		|		
		|
        |-  scrapy.cfg				ȫ�������ļ�

### ����
Spiders       : �����Engine URL��ַ, ���߸�����Responses, �ռ�Data
Middlewares   : �м��
Scrapy Engine : ����������ͨѶ, �Լ��źź����ݵĴ���
Scheduler     : ������. �������Request����, ����һ����ʽ���������黹��Engine
Downloader    : ��������������ҳ, ����Responses����Engine
Item Piperline: ������Item, ������������ݵĺ��ڴ���


## ��ʼ��
* cd projectĿ¼
* scrapy startproject ProjectName	����project
* scrapy genspider py�ļ��� *.com	scrapyģ��. ָ��������
* scrapy crawl crawlName			��ʼִ������ΪcrawlName������