import random
# pip install pygame
import pygame
import win32api
import win32con

# 初始化
pygame.init()
# 窗口标题
pygame.display.set_caption('jigsaw_puzzle拼图游戏2019')
# 窗口大小
s = pygame.display.set_mode((1200, 600))

# # 加载背景音乐
# pygame.mixer.music.load(music_base_path + "music.mp3")
# # 设置音量
# pygame.mixer.music.set_volume(0.1)
# # 循环播放
# pygame.mixer.music.play(-1, 0)


#绘图地图
imgMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
 
#判断胜利的地图
winMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
 
#游戏的单击事件
def click(x, y, map):
    if y - 1 >= 0 and map[y - 1][x] == 8:
        map[y][x], map[y - 1][x] = map[y - 1][x], map[y][x]
    elif y + 1 <= 2 and map[y + 1][x] == 8:
        map[y][x], map[y + 1][x] = map[y + 1][x], map[y][x]
    elif x - 1 >= 0 and map[y][x - 1] == 8:
        map[y][x], map[y][x - 1] = map[y][x - 1], map[y][x]
    elif x + 1 <= 2 and map[y][x + 1] == 8:
        map[y][x], map[y][x + 1] = map[y][x + 1], map[y][x]
 
#打乱地图
def randMap(map):
    for i in range(1000):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        click(x, y, map)
 
# 加载图片
img = pygame.image.load('E:\code\py_tools\shili.jpg')
#随机地图
randMap(imgMap)
#游戏主循环
while True:
    #延时32毫秒,相当于FPS=30
    pygame.time.delay(32)
    for event in pygame.event.get():
        # 窗口的关闭事件
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:      #鼠标单击事件
            if pygame.mouse.get_pressed() == (1, 0, 0):     #鼠标左键按下
                mx, my = pygame.mouse.get_pos()     #获得当前鼠标坐标
                if mx<498 and my <498:      #判断鼠标是否在操作范围内
                    x=int(mx/166)       #计算鼠标点到了哪个图块
                    y=int(my/166)
                    click(x,y,imgMap)   #调用单击事件
                    if imgMap==winMap:  #如果当前地图情况和胜利情况相同,就print胜利
                        print("胜利了！")
                        #win32api.MessageBox(win32con.NULL, '胜利了！', '胜利了', win32con.MB_OK) 
                        #sys.exit()
    #背景色填充成灰色
    s.fill((217, 217, 217))
    #绘图
    for y in range(3):
        for x in range(3):
            i = imgMap[y][x]
            if i == 8:      #8号图块不用绘制
                continue
            dx = (i % 3) * 166      #计算绘图偏移量
            dy = (int(i / 3)) * 166
            s.blit(img, (x * 166, y * 166), (dx, dy, 166, 166))
    # 画参考图片
    s.blit(img, (600, 0))
    # 刷新界面
    pygame.display.flip()