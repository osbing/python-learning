"""
酷狗TOP500_排行榜_乐库频道_酷狗网
"""

from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}

def get_info(url):
    """获取页面信息"""
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    ranks = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
    titles = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    links = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')

    # print(type(links))
    for rank,title,time,link in zip(ranks,titles,times,links):
        data = {
            'rank':rank.get_text().strip(),
            'singer':title.get_text().strip().split(' - ')[0],
            'song':title.get_text().strip().split(' - ')[-1],
            'time':time.get_text().strip(),
            'link':link.get('href') # 获取 Tag <a /a> 的属性
        }
        print(data)

if __name__ == '__main__':
    # 酷狗TOP500_排行榜_乐库频道_酷狗网
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i))
            for i in range(1,24)
    ]
    for url in urls:
        get_info(url)
        time.sleep(1)