# findall()函数 逐行匹配
import re
a = 'xxIxxjshdxxlovexxsffaxxpythonxx'
infos = re.findall('xx(.*?)xx',a) # (.*?)非贪心算法
print(infos)
b = 'one1two2trhree3'
infos_1 = re.findall('\d+',b)
print(infos_1)

# search()函数
# re.match(pattern, string, flags=0)
import re
a = 'one1two2three3'
infos = re.search('\d+',a) # [0-9]
print(infos) #search 方法返回的是正则表达式对象 <re.Match object; span=(3, 4), match='1'>
print(infos.group()) # group 方法获取信息 字符串

# sub()函数
# re.sub(pattern, repl, string, count=O, flags=O)
import re
phone = '123-4567-1234'
new_phone = re.sub('\D','',phone) # [^0-9]
print(new_phone)


# <span class="result_price">&#165;<i>400</i>起/晚</span>
import re
import requests
headers = {
    'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'
    }
url = 'http://bj.xiaozhu.com/'
res = requests.get(url,headers=headers)
# 正则获取价格
prices = re.findall('<span class="result_price">&#165;<i>(.*?)</i>起/晚</span>',res.text)
for price in prices:
    print(price)


# re 模块修饰符
import re
a = '<div>指数</div>'
word = re.findall('<div>(.*?)</div>',a)
print(word)
b = '''<div>指数 
</div>'''
word_1 = re.findall('<div>(.*?)</div>',a,re.S) #re . S 用于跨行匹配
print(word_1[0].strip()) # 数据清洗 去除换行符 跨行匹配的结果会有一个换行符， 这种数据需要清洗才能存入数 据库
