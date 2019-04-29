# 安居客
"""
Datetime 2019/4/29
"""
from bs4 import BeautifulSoup
import requests
import time
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}

info_lists = []

def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('#list-content > div > div.zu-info > h3 > a')
    prices = soup.select('#list-content > div > div.zu-side > p > strong')
    addresses = soup.select('#list-content > div > div.zu-info > address')

    for price,address,title in zip(prices,addresses,titles):
        data = {
            'price':price.get_text(),
            'address':address.get_text().strip().replace('\xa0\xa0\n','').replace(' ',''),
            'title':title.get_text().strip()
        }
        info_lists.append(data)
        print(data)

if __name__ == '__main__':
    urls = ['https://gz.zu.anjuke.com/fangyuan/tianhe/p{}/'.format(i) for i in range(1,2)] # 天河区
    for url in urls:
        get_info(url)
    for info_list in info_lists:
        with open('C:/GitHub/python-learning/workspace/20190423/anjuke.txt','a+',encoding='utf-8') as f:
            try:
                f.write(info_list['price']+','),
                f.write(info_list['address']+','),
                # f.write(info_list['title']+'\n')
                f.write(info_list['title']+'\n')
            except UnicodeEncodeError:
                pass

    # 创建表格和表头
    with open('C:/GitHub/python-learning/workspace/20190423/anjuke.csv','wt',newline='',encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerow(('Price','Address','Title')) # 写入 header

    for info_list in info_lists:
        # newline='' 避免空行
        with open('C:/GitHub/python-learning/workspace/20190423/anjuke.csv','a+',newline='',encoding='utf-8') as fp:
            writer = csv.writer(fp)
            price = info_list['price']
            address = info_list['address']
            title = info_list['title']
            writer.writerow((price,address,title))
            # writer.writerow((info_list['price'],info_list['address'],info_list['title']))