#-*- coding:utf-8 -*-

# lxml 解析HTML文档
# https://book.douban.com/top250
import requests
from lxml import etree
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}

def get_info(url,file_path):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    # //*[@id="content"]/div/div[1]/div/table[2]/tbody/tr/td[2]/div[1]/a
    infos = selector.xpath('//tr[@class="item"]')  # 取大标签，以此循环
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        # //*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/p[1]
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0].strip(' ')
        publisher = book_infos.split('/')[-3].strip(' ')
        date = book_infos.split('/')[-2].strip(' ')
        price = book_infos.split('/')[-1].strip(' ')
        rate = info.xpath('td/div/span[2]/text()')[0].strip(' ')
        comments = info.xpath('td/p/span/text()')
        comment = comments[0].strip(' ') if len(comments) != 0 else '空'
        print(name,author,publisher,date,price,rate,comment,url)
        with open(filename_path,'a+',newline='',encoding='utf-8') as fp:            
            writer = csv.writer(fp)
            writer.writerow((name,author,publisher,date,price,rate,comment,url)) # 写入数据

# print(infos)
# print(html) # <Element html at 0x27fdf70c908>
# result = etree.tostring(selector) # lxml 自动修正HTML代码
# result_one = etree.tostring(html,pretty_print=True)
# print(result) 
# print(result_one)

if __name__ == '__main__':
    urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)] # range(1,12)
    filename_path = 'C:/GitHub/python-learning/workspace/20190423/doubanbook.csv'
    with open(filename_path,'wt',newline='',encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerow(('name','author','publisher','date','price','rate','comment','url')) # 写入header
    for url in urls:
        # print(url)
        get_info(url,filename_path)