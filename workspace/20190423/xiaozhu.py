from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}

def judgment_sex(class_name):
    """判断性别"""
    if class_name == ['member_ico1']:
        return '女'
    else:
        return '男'

def get_links(url):
    """循环出详细页URL，并调用get_info()函数"""
    # <a target="_blank" href="http://bj.xiaozhu.com/fangzi/38696965403.html" class="resule_img_a">
    #           <img class="lodgeunitpic" title="近三里屯朝阳大悦城，距地铁200m，可住4人" data-growing-title="38696965403" src="https://image.xiaozhustatic3.com/12/51,0,34,2124,1800,1201,5c7f8134.jpg" lazy_src="finish" alt="近三里屯朝阳大悦城，距地铁200m，可住4人" style="height: 198px;">
    #     </a>
    wb_data = requests.get(url,headers=headers)
    print(wb_data)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get("href") #循环出详细页URL
        get_info(href) # 调用get_info()函数

def get_info(url):
    """获取网页信息的函数"""
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.pho_info > h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')

    for title, address, price, img, name, sex in zip(titles, addresses, prices, imgs, names, sexs):
        """获取信息并通过字典的信息打印"""
        data = {
            'title':title.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text(),
            'img':img.get("src"),
            'name':name.get_text(),
            'sex':judgment_sex(sex.get("class"))
        }
        print(data)

if __name__ == '__main__':
    """程序主入口"""
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) 
    for number in range(1,3)
    ] 
    for single_url in urls:
        """注意反爬"""
        get_links(single_url)
        time.sleep(2)