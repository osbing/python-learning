# Date 2019/5/5
# 需要爬取的信息有：用户 ID、用户等级、用户性别、发表段子文字信息，好笑 数量和评论数量
# ID: <h2>南九</h2>
# 用户等级：<div class="articleGender womenIcon">27</div> <div class="articleGender manIcon">31</div>
# class="articleGender manIcon
# <div class="content">
# <span>春天到了，树叶都绿了。<br>咯咯咯......<br>依然记得去年春天，单位领导带我们出去玩，看到一棵榆树，开满了榆树钱儿。<br>领导就跟我们说:你们年轻，没赶上苦的时候，我小时候，经常吃不饱，所以，就用榆钱儿来充饥。<br>说着，领导顺手抓了一把榆钱儿放进嘴里，一边嚼着一边说:那时候吃着挺甜的，现在生活条件好了，吃不出那个味儿了！<br>可是，我亲眼看见他抓了一把榆树叶塞进嘴里......
# </span>
# </div>
# 好笑：<span class="stats-vote"><i class="number">873</i> 好笑</span>
# 评论数量：<i class="number">39</i>
# <span class="stats-comments">
# <i class="number">22</i> 评论
# </a>
# </span>

# https://www.qiushibaike.com/text/page/2/
import re
import requests
import time

headers = {
    'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'
}

info_lists = []
yet_lists = [] # 已爬列表

def judgment_sex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'

def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
        levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)
        sexs = re.findall('<div class="articleGender (.*?)">',res.text,re.S)
        contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
        laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',res.text,re.S)
        comments = re.findall('<span class="stats-comments">.*?<i class="number">(\d+)</i> 评论',res.text,re.S)
        for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
            info = {
                'id':id.strip('\n'),
                'level':level,
                'sex':judgment_sex(sex),
                'content':content.strip('\n'),
                'laugh':laugh,
                'comment':comment
            }
        info_lists.append(info)

        # print(info_lists)
    else:
        print('出错')
        pass

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,50)]
    for url in urls:
        get_info(url)
        yet_lists.append(url)
        # print(yet_lists)
        # time.sleep(1)
    info_lists = sorted(info_lists, key=lambda x : x['laugh'], reverse=False)  # 对列表中的字典根据 laugh 的值按降序排序
    # print(info_lists)

    for info_list in info_lists:
        with open('C:/GitHub/python-learning/workspace/20190423/qiushi.txt', 'a+', encoding='utf-8') as f:
            try:
                f.write('id:' + info_list['id'] + ',')
                f.write('level:' + info_list['level']+ ',')
                f.write('sex:' + info_list['sex']+ ',')
                f.write('content:' + info_list['content']+ '\n')
                f.write('laugh:' + info_list['laugh']+ ',')
                f.write('comment:' + info_list['comment']+ '\n\n')
            except UnicodeEncodeError:
                pass