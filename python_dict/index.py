# -*- coding: UTF-8 -*-
"""
python开发单词查询系统
file：index.py #主文件
file：data.json #单词列表库
"""
import json
from difflib import get_close_matches

a = ['one', 'two', 'three']
b = get_close_matches('one', a, cutoff=0.5)
print(b)

data = json.load(open("data.json", "r", encoding="utf-8"))
#print(data.keys()) #键值
#print(data['one'])
#print('one' in data)

def translate(word):
    word = word.lower() #转换为信息，避免大小写识别
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.5)) > 0:
        yn =input("您要查询的是不是：%s ?如果是：请输入Yes 否则输入No: " % get_close_matches(word, data.keys(), cutoff=0.5)[0])
        yn = yn.lower()
        if yn == 'yes':
            return data[get_close_matches(word, data.keys(), cutoff=0.5)[0]]
        elif yn == 'no':
            return '您想要查询的单词不存在！'
        else:
            return '请输入指定的指令'
    else:
        return '您想要查询的单词不存在！'
# print(translate('two'))

word = input("请输入要查询到的单词：")
output = (translate(word))
if type(output) == list: #优化列表输出 如果是列表则遍历输出
    for item in output:
        print(item)
else:
    print(output)
