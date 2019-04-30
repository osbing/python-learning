x = [
    {'price': '1810', 'address': '庙元六巷小区天河-东圃庙元六巷', 'title': '庙元六巷小区东圃设计师为您精心打造 高品质生活蜗居'},
    {'price': '1660', 'address': '保利金融大都汇天河-金融黄埔大道中666号', 'title': '保利金融大都汇金融这就是你一直在找的房子 家电齐全 欲租从速'},
    {'price': '1650', 'address': '长湴新村天河-长湴长湴东路', 'title': '长湴新村长湴主卧带飘窗 干净整洁 拎包入住'},
    {'price': '1980', 'address': '联发名苑天河-粤垦粤垦路490-494号', 'title': '联发名苑 走路三天河公园地铁站 交通便利 房价透明'}
    ]
sorted_x = sorted(x, key=lambda x : x['price'], reverse=True)  # 对列表中的字典根据priced的值按降序排序
print(sorted_x)