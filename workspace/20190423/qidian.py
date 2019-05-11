#-*- coding:utf-8 -*-

# pip3 install xlwt

# https://www.qidian.com/
import xlwt
import requests
from lxml import etree
import time
# book = xlwt.Workbook(encoding='utf-8')
# sheet = book.add_sheet('Sheet1')
# sheet.write(0,0,'python')
# sheet.write(1,1,'love')
# book.save('C:/GitHub/python-learning/workspace/20190423/test.xls')


# https://www.qidian.com/all/?page=3
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}
all_info_list = []

def get_info(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li') # /html/body/div[1]/div[5]/div[2]/div[2]/div/ul
    for info in infos:
        title = info.xpath('div[2]/h4/a/text()')[0] # /html/body/div[1]/div[5]/div[2]/div[2]/div/ul/li[1]/div[2]/h4/a
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]  # /html/body/div[1]/div[5]/div[2]/div[2]/div/ul/li[1]/div[2]/p[1]/a[1]
        style_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0] # /html/body/div[1]/div[5]/div[2]/div[2]/div/ul/li[1]/div[2]/p[1]/a[2]
        style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        style = style_1+'.'+style_2
        complete = info.xpath('div[2]/p[1]/span/text()')[0].strip()
        introduce = info.xpath('div[2]/p[2]/text()')[0].strip() # /html/body/div[1]/div[5]/div[2]/div[2]/div/ul/li[1]/div[2]/p[2]/text()
        word = info.xpath('div[2]/p[3]/span/text()')[0].strip('万字') # /html/body/div[1]/div[5]/div[2]/div[2]/div/ul/li[1]/div[2]/p[3]/span/span
        print(title,author,style,complete,introduce,word)
        info_list = [title,author,style,complete,word,introduce]
        all_info_list.append(info_list)

if __name__ == '__main__':
    urls = ['https://www.qidian.com/all/?page={}'.format(str(i)) for i in range(0,3)]
    for url in urls:
        get_info(url)
    header = ['title','author','style','complete','word','introduce'] # 定义表头
    book = xlwt.Workbook(encoding='utf-8') # 创建工作簿
    sheet = book.add_sheet('Sheet1') # 创建工作表
    for h in range(len(header)):
        sheet.write(0, h, header[h]) # 写入表头
    i = 1
    for list in all_info_list:
        j = 0
        for data in list:
            sheet.write(i, j, data)
            j += 1
        i += 1 #写入爬虫数据
    book.save('C:/GitHub/python-learning/workspace/20190423/xiaoshuo.xls')