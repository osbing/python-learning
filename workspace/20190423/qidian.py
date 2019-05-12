#-*- coding:utf-8 -*-

# pip3 install xlwt
# pip install fonttools
# https://www.qidian.com/
# 字数反爬 https://blog.csdn.net/qq_35741999/article/details/82018049 
import xlwt
import requests
from lxml import etree
import time
import re
from fontTools.ttLib import TTFont
from io import BytesIO
from pyquery import PyQuery as pq

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

def get_font(url):
    """ 字数反爬 解析字体 """
    response = requests.get(url)
    font = TTFont(BytesIO(response.content))
    cmap = font.getBestCmap()
    font.close()
    return cmap

def get_encode(cmap,values):
    """ 字数反爬 解析数值 """
    WORD_MAP = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','period':'.'}
    word_count = ''
    for value in values.split(';'):
        value = value[2:]
        key = cmap[int(value)]
        word_count += WORD_MAP[key]
    return word_count

def get_info(url):
    """ 爬虫 """
    try:
        #  """ 获取字体文件链接 """
        response = requests.get(url).text   #获取当前页面的html
        doc = pq(response)
        classattr = doc('p.update > span > span').attr('class') #获取当前字体文件名称
        pattern = '</style><span.*?%s.*?>(.*?)</span>'%classattr
        numberlist = re.findall(pattern,response) #获取当前页面所有被字数字符
        fonturl = doc('p.update > span > style').text() #获取当前包含字体文件链接的文本
        url_font = re.search('woff.*?url.*?\'(.+?)\'.*?truetype',fonturl).group(1) #通过正则获取当前页面字体文件链接
        cmap = get_font(url_font) #字数反爬 解析字体
        i = 0

        # 开始爬虫
        html = requests.get(url,headers=headers)
        selector = etree.HTML(html.text)
        infos = selector.xpath('//ul[@class="all-img-list cf"]/li') 
        for info in infos:
            title = info.xpath('div[2]/h4/a/text()')[0] 
            author = info.xpath('div[2]/p[1]/a[1]/text()')[0]  
            style_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0] 
            style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
            style = style_1+'.'+style_2
            complete = info.xpath('div[2]/p[1]/span/text()')[0].strip()
            introduce = info.xpath('div[2]/p[2]/text()')[0].strip() 
            # word = info.xpath('div[2]/p[3]/span/span/text()')[0].strip('万字') 
            word_count = get_encode(cmap,numberlist[i][:-1])
            i += 1
            print(title,author,style,complete,word_count,introduce)
            info_list = [title,author,style,complete,word_count,introduce]
            all_info_list.append(info_list)
    except:
        pass
    time.sleep(1)

if __name__ == '__main__':
    urls = ['https://www.qidian.com/all/?page={}'.format(str(i)) for i in range(0,10)]
    for url in urls:
        get_info(url)
    header = ['title','author','style','complete','word_count','introduce'] # 定义表头
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