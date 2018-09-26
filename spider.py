#有些内容不适用于python3. 基于py2的代码
	#python3
import requests

	#python2
import ssl
import cookielib
import urllib

import json
import jsonpath
import random
import re
from lxml import etree		#xpath库
import beautifulsoup4 as bs4
#默认User-Agent: Python-urllib

userAgnets = ["", "", ""]
acceptLans = ["", "", ""]

userAgent = random.choise(userAgnets)
acceptLan = random.choise(acceptLans)

#--------------------------------url编码
'''python2
urllib.urlencode("str")	#将汉字和空格转换为url编码
urllib.urldecode("str")	#将url编码转为字符
'''

urllib.parse.quote("str")	#编码
urllib.parse.unquote("str", encoding="utf-8")	#解码
#--------------------------------忽略ssl检查
'''python2
context = ssl._create_unverified_context()
'''

并不知道
#--------------------------------构建请求头
'''python2
requests = url2.Request("urllink", data=None) #data不为空是Post, 为空是Get

#添加修改一个请求头
requests.add("User-Agent", userAgnet)
requests.add("Accept-Language", acceptLan)
print(request.get_header("User-agent"))	#获取已有的请求头, 必须: 首字母大写其余小写
'''

headers = {"User-Agent":userAgent}
headers["Accept-Language"] = acceptLan
#---------------------------------向指定url发送请求, 返回服务器的类文件对象
'''python2
resp = url2.urlopen(requests, context=context)
print(resp.getcode())	#响应码
print(resp.geturl())	#返回实际url
print(resp.getinfo())	#返回服务器报头

#类文件对象支持python文件对象的操作
#read() or something
html = resp.read()
'''

sess = requests.Session()
html = sess.get("link", headers=headers, timeout=40).text	#timeout单位:毫秒
html = sess.put("link", data=data, headers=headers).content	#put 字典, content为二进制流
#---------------------------------cookie
'''python2
cookie = cookielib.CookieJar()
handler = url2.HTTPCookieProcessor(cookie)
data = urllib.urlencode([("User-Agent", ""),])
request = url2.Request(url, data=data)	#通过登陆接口, post 账户密码, 生成cookie
'''

sess: 会话自动保存Cookie
#------------------------------------------------------------------------------------------------
#---------------------------------xpath
xp = etree.HTML(html)	#解析html文档
list = xp.xpath("//book")	#xpath规则
node = list.xpath("./div")	#可以一直xpath下去. xpath返回一个列表

#---------------------------------Regex
patten = re.compile("<div\sclass=''(.*?)</div>", re.S)	#re.S全文匹配, re.I忽略大小写
content = patten.findall(html)	#list

#---------------------------------JsonPath
unicodestr = json.loads(html)	#转换为python2的Unicode格式
jsondata = jsonpath.jsonpath(unicodestr, "$..name")	#jsonpath规则
array = json.dumps(jsondata, ensure_ascii=False)	#unicode数据

#---------------------------------BeautifulSoup4	慢速, 载入DOM. 但支持CSS选择器, 也最为简单
soup = BeautifulSoup4(html, "lxml")	#指定解析器解析html文档, 转为树形结构
soup.title	#html的title标签
soup.title.attr	#title标签的属性
soup.title['class']	#title的class
soup.title.name.string	#获取name对应的string
soup.title.contents	#子节点+本身列表
soup.title.children	#子节点列表
soup.title.descnedans	#所有深度的子节点
soup.select().get_text()	#select支持伪类选择器
soup.find("input",attrs={"class":"somep"})	#特定对象查找

#------------------------------------------------------------------------------------------------
#---------------------------------自定义Handler对象, 构建opener发送.urlopen是内置的opener
'''python2
handler = url2.HTTPHandler(debuglevel=1) #debuglevel=1 打印收发包信息
proxy = url2.ProxyHandler({"https":"usrname:password@127.0.0.1:80"})	#代理
opener = url2.build_opener(handler)
resp = opener.open(requests)
'''

并不知道
#---------------------------------401
'''python2
passwdMgr = url2.HTTPPasswordMgrWithDefaultRealm()	#代理用ProxyPass...Realm()
passwdMgr.add_password(None, webserver, usrname, passwd)
handler = url2.HTTPBasicAuthHandler(passwdMgr)
'''

并不知道
#---------------------------------验证码

使用pytesseract