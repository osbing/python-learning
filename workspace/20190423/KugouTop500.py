"""
酷狗TOP500_排行榜_乐库频道_酷狗网
"""

from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}

info_lists = [] # 初始化列表，用于装入爬虫信息

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
        # print(data)
        info_lists.append(data) # 循环数据并append到list中

if __name__ == '__main__':
    # 酷狗TOP500_排行榜_乐库频道_酷狗网
    print(time.ctime())
    t1 = time.process_time()
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i))
            for i in range(1,24) # 2~24
    ]
    for url in urls:
        get_info(url) # 循环调用爬虫信息函数
        time.sleep(1)
    for info_list in info_lists:
        # 写入TXT
        with open('C:/GitHub/python-learning/workspace/20190423/KugouTOP500.txt','a+',encoding='utf-8') as f:
            try:
                f.write(info_list['rank']+',')
                f.write(info_list['singer']+',')
                f.write(info_list['song']+',')
                f.write(info_list['time']+',')
                f.write(info_list['link']+'\n')
                # result 1,陈雪凝,绿色,4:29,https://www.kugou.com/song/txskm8f.html
            except UnicodeEncodeError:
                pass # pass编码错误
        # print(info_list)
    print(time.ctime())
    t2 = time.process_time()
    t = t2 - t1
    print('Cost: ' + str(t) + ' s')