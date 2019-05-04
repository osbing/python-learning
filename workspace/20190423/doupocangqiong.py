# Date 2019/5/4

import requests
import re
import time

headers = {
    'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'
}

def get_info(url):
    res = requests.get(url,headers)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
        for content in contents:
            print(content)
            with open('C:/GitHub/python-learning/workspace/20190423/doupo.txt','a+') as f:
                f.write(content+'\n')
    else:
        pass

if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,3)]
    for url  in urls:
        get_info(url)
        time.sleep(1)