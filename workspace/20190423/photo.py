from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import time

headers = {
    'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

lists = []

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('article > a > img')
    for img in imgs:
        photo = img.get('src').split('?')[0]
        # print(photo)
        # https://images.pexels.com/photos/2099265/pexels-photo-2099265.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260
        lists.append(photo)
    count = 1
    for item in lists:
        # print(item.split('?')[0])
        print('Downloading...' + str(count))
        data = requests.get(item, headers=headers)
        path = 'C:/GitHub/python-learning/workspace/20190423/photo/'
        with open(path + item.split('/')[-1], 'wb') as fp:
            fp.write(data.content)
        count += 1

if __name__ == '__main__':
    urls = ['https://www.pexels.com/search/book/?page={}'.format(str(i)) for i in range(1,2)]
    start = time.time()
    pool = Pool(processes=4)
    pool.map(get_info, urls)
    pool.close()
    pool.join()
    end = time.time()
    print(end - start)