import requests as url2
import urllib
from itertools import permutations
import re
import json

urls = "https://translate.google.cn/#en/zh-CN/"
url = "http://fy.iciba.com/ajax.php?a=fy"

def spider(s):
        urs = {
                'content-type': 'application/json, text/javascript, */*; q=0.01',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Connection': 'keep-alive',
                'Origin': 'http://fy.iciba.com',
                'Host': 'fy.iciba.com',
                'X-Requested-With': 'XMLHttpRequest'
                
               }
        data = {'f':'en','t':'zh','w':s}
        requ = url2.post(url, data=data, headers=urs)
        requ.raise_for_status()
        requ.encoding = requ.apparent_encoding

        patten = re.compile('"word_mean":.*]+')
        content = patten.findall(requ.text)
        content = "".join(content).encode('utf-8').decode('unicode_escape')
        if content == "":
                return
        print(s,content)

if __name__ == "__main__":
        alphabeta = input("the origin alphabeta: ")
        s = list(alphabeta)
        for i in permutations(s):
                spider("".join(i))
        
