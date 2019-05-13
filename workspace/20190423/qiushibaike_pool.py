# 当数据量大，需要追求效益时，Lxml 是最好的选择

import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import time
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}

# user_lists = []
def re_scraper(url):
    """ 正则 """
    res = requests.get(url,headers=headers)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    for id in ids:
        info = {
            'id':id
        }
    # print(info)
    return info

def bs_scraper(url):
    """ BeautifulSoup """
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    ids = soup.select('a > h2')
    for id in ids:
        info = {
            'id':id.get_text()
        }
    # print(info)
    return info

def lxml_scraper(url):
    """ Lxml """
    res = requests.get(url,headers=headers)
    selector = etree.HTML(res.text)
    # print(selector)

    url_infos = selector.xpath('//div[@class="article block untagged mb15 typs_hot"]')
    # //*[@id="qiushi_tag_121790374"]/div/a[2]/h2 #当前节点
    # id_1 = selector.xpath('//*[@id="qiushi_tag_121790374"]/div/a[2]/h2/text()') # /text()获取标签中的文字信息
    # id = selector.xpath('//*[@id="qiushi_tag_121790374"]/div/a[2]/h2/text()')[0] # 将列表结构通过切片获取字符串数据结构
    try:
        for url_info in url_infos:
            id = url_info.xpath('div/a[2]/h2/text()')[0].strip('\n')
            info ={
                'id':id
            }
            # user_lists.append(id)
            return info
    except IndexError:
        pass

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,36)]
    for name,scraper in [('Regu',re_scraper),('BeaS',bs_scraper),('Lxml',lxml_scraper)]:
        # 循环三种方法
        start_1 = time.time()
        for url in urls:
            scraper(url)
        end_1 = time.time()
        print('1个进程',name,end_1-start_1)

        start_2 = time.time()
        pool = Pool(processes=2)
        pool.map(scraper,urls)
        end_2 = time.time()
        print('2个进程',name,end_2-start_2)

        start_3 = time.time()
        pool = Pool(processes=4)
        pool.map(scraper,urls)
        end_3 = time.time()
        print('4个进程',name,end_3-start_3,end='\n')
        time.sleep(1)