
import requests
from lxml import etree

headers = {
    'accept':'text/html, */*; q=0.01',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
def get_info(url,page):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//div[@class="content"]')
    author_infos = selector.xpath('//div[@class="info"]')
    id_infos  = selector.xpath('//ul[@class="note-list"]/li/@id')
    for info in infos:
        title = info.xpath('a/text()')
        if len(title) is not 0:
            print(title)
        else:
            pass
    for author_info in author_infos:
        nickname = author_info.xpath('a[@class="nickname"]/text()')
    if len(nickname) is not 0:
        data_type = author_info.xpath('span/@data-type')
        data_time = author_info.xpath('span/@data-datetime')
        # content = author_info.xpath('/text()')
        print(nickname,data_type,data_time)
    else:
        pass

    user_id = url.split('/')[4]
    if url.find('page='):
        page += 1
    if len(id_infos) > 1:
        feed_id = id_infos[-1]
        max_id = feed_id.split('-')[1]
        next_url = 'https://www.jianshu.com/users/%s/timeline?max_id=%s&page=%s' % (user_id, max_id, page)
        get_info(next_url, page)


if __name__ == '__main__':
    url = 'https://www.jianshu.com/users/8f5b45499715/timeline'
    get_info(url, 0)