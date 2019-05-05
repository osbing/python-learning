# lxml 解析HTML文档
# https://book.douban.com/top250
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}
# url = 'https://book.douban.com/top250'

def get_info(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td]/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/@text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')[0]
        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments) != 0 else '空'
        print(name,url,author,publisher,date,price,rate,comment)

# print(infos)
# print(html) # <Element html at 0x27fdf70c908>
# result = etree.tostring(selector) # lxml 自动修正HTML代码
# result_one = etree.tostring(html,pretty_print=True)
# print(result) 
# print(result_one)

if __name__ == '__main__':
    urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)] # range(1,12)
    for url in urls:
        print(url)
        get_info(url)