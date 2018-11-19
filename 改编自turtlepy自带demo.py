"""
改编自turtle.py自带demo
执行 python -m turtledemo 命令查看系统内置demo的源码

    绘制：需要通过import turtle引入绘制图形库turtle库

    注意：1.全文中的 turtle.xxx()中的turtle本质是该海龟屏幕上默认的海龟实例对象,他等价于turtle.getturtle()返回的对象实例.即任何turtle.xxx()函数都可以写成turtle.getturtle.xxx()
          2.屏幕正中心为(0,0)点
"""
import turtle
import time


def demo1():
    # 恢复默认位置和默认方向,保留当前海龟箭头图标(此时就是普通箭头)
    turtle.reset()
    turtle.tracer(True)
    # 画笔抬起
    turtle.pu()
    # 画笔向后100像素
    turtle.bk(100)
    # 画笔放下
    turtle.pd()
    # 设置画笔线条粗细为3,同turtle.width(3)
    turtle.pensize(3)
    # 绘制3个正方形; 填充最后一个(i 从 0 - 2循环3次)
    for i in range(3):
        print("当前i=", i)

        if i == 2:
            # 最后一个正方形开始填充
            turtle.begin_fill()

        # 写字标识当前再画第几个正方形
        turtle.write(i + 1, False, align="right")

        # 画正方形
        draw_square(turtle.getturtle())

        if i == 2:
            # 绘制完正方形后将pencolor和fillcolor设置成褐红色
            turtle.color("maroon")
            # 最后一个正方形结束填充
            turtle.end_fill()

        # 每次画完正方形画笔抬起,然后向前移动30像素再放下
        turtle.pu()
        turtle.fd(30)
        turtle.pd()

    # 设置画笔线条粗细为1,同turtle.width(1)
    turtle.pensize(1)
    # 将pencolor和fillcolor设置成黑色
    turtle.color("black")

    # move out of the way
    turtle.tracer(False)
    # 画笔抬起
    turtle.pu()
    # 右转90度此时方向向下
    turtle.rt(90)
    # 向前(即向下)移动100像素
    turtle.fd(100)
    # 右转90度此时方向向左
    turtle.rt(90)
    # 向前(即向左)移动100像素
    turtle.fd(100)
    # 右转180度此时方向向右
    turtle.rt(180)
    # 画笔放下
    turtle.pd()
    # 绘制一些文本
    turtle.write("画楼梯", True)
    turtle.write("start", True)
    # 将pencolor和fillcolor设置成红色
    turtle.color("red")
    # 画5个楼梯(从0-4遍历),最后heading()为0.0表示方向向右
    for i in range(5):
        turtle.fd(20)
        turtle.lt(90)
        turtle.fd(20)
        turtle.rt(90)
    turtle.tracer(True)
    # 绘制5个填充的楼梯
    turtle.begin_fill()
    for i in range(5):
        turtle.fd(20)
        turtle.lt(90)
        turtle.fd(20)
        turtle.rt(90)
    # 完成填充,因为此时的fillcolor为red红色,所以以红色进行填充
    turtle.end_fill()
    # more text


def switchpen(_turtle):
    """
    间断效果
    :param _turtle: 将被处理的turtle对象
    """
    if _turtle.isdown():
        _turtle.pu()
    else:
        _turtle.pd()


def draw_square(_turtle):
    """
    画边长20像素的正方形
    :param _turtle: 将被处理的turtle对象
    """
    # 方法1
    """
    old = _turtle.heading()
    _turtle.setheading(315)
    _turtle.circle(15, None, 4)
    _turtle.setheading(old)
    """
    # 方法2
    for _ in range(4):
        _turtle.fd(20)
        _turtle.lt(90)


def demo2():
    """Demo of some new features."""
    # 使用最慢速度 0最快,1-10逐渐加快
    turtle.speed(1)
    # 隐藏画笔(即海龟箭头),同 turtle.hideturtle()。此时只要画笔是按下状态，虽然隐藏了但是还是能绘制图形的
    #turtle.ht()
    # 显示画笔,同 turtle.showturtle()
    #turtle.st()
    # 设置画笔线条粗细为3,同turtle.width(3)
    turtle.pensize(3)
    # 设置海龟箭头当前方向角度(当前模式下海龟箭头当前位置指向(0,0)点的向量角度),turtle.towards(0, 0)其实是当前方向的反方向
    turtle.setheading(turtle.towards(0, 0))
    # 计算半径(海龟箭头当前位置到(0,0)位置距离的一半)
    radius = turtle.distance(0, 0)/2.0
    # 海龟箭头右转90度,即以海龟箭头当前位置到(0,0)为直径画
    turtle.rt(90)
    # 画18次角度为10度的小段圆弧,画笔每按下画一小段就再抬起移动一小段
    for _ in range(18):
        switchpen(turtle.getturtle())
        turtle.circle(radius, 10)
    turtle.write("wait a moment...")

    # 等待2秒
    time.sleep(2)

    # 撤销所有
    while turtle.undobufferentries():
        turtle.undo()
    # 清屏并将画笔位置和方向恢复到初始状态并保持画笔形状不变，即位置到原点(0, 0)，因为模式是"standard"方向恢复向右,"standard"/"world"模式方向也恢复到默认的向右,"logo"模式方向恢复到默认的向上
    turtle.reset()
    # 海龟箭头左转90度
    turtle.lt(90)
    turtle.colormode(255)
    # 定义等边三角形默认的边长
    laenge = 10
    turtle.pencolor("green")
    # 设置画笔线条粗细为3, 同turtle.width(3)
    turtle.pensize(3)
    # 海龟箭头左转180度
    turtle.lt(180)
    # i为-2 到15 共遍历18次,之所以i有负数,是因为内循环中turtle.fillcolor(255-15*i, 0, 15*i)中的15*i不能超过255(即colormode的值)
    for i in range(-2, 16):
        print("当前i=", i)
        # 后15次画的图形进行填充,每次填充色不同
        if i > 0:
            turtle.begin_fill()
            turtle.fillcolor(255-15*i, 0, 15*i)
        # 画等边三角形
        for _ in range(3):
            turtle.fd(laenge)
            turtle.lt(120)
        # 后15次画的图形填充完毕
        if i > 0:
            turtle.end_fill()

        # 每画完一个等边三角形,等边三角形的变成增加10像素,并且角度左转15度
        laenge += 10
        turtle.lt(15)

        # 达到 慢->快->慢->快 的效果 (速度值>10 则被置为0即最快速度)
        turtle.speed((turtle.speed()+1) % 12)

    # 海龟箭头左转120度
    turtle.lt(120)
    # 画笔抬起
    turtle.pu()
    # 向前移动70像素
    turtle.fd(70)
    # 海龟箭头向右转30度
    turtle.rt(30)
    # 画笔放下
    turtle.pd()
    # pencolor设置成红色并且fillcolor设置成黄色
    turtle.color("red", "yellow")
    # 速度设置成最快
    turtle.speed(0)
    # 画图形并填充
    turtle.begin_fill()
    for _ in range(4):
        # 绘制1/4圆
        turtle.circle(50, 90)
        # 右转90度
        turtle.rt(90)
        # 前移30像素
        turtle.fd(30)
        # 右转90度
        turtle.rt(90)
    # 图形填充完毕
    turtle.end_fill()
    # 海龟箭头左转90度
    turtle.lt(90)
    # 画笔抬起
    turtle.pu()
    # 向前移动30像素
    turtle.fd(30)
    # 画笔放下
    turtle.pd()
    # 海龟箭头图标设置成海龟
    turtle.shape("turtle")
    # 获取(默认的)第一个Turtle实例对象
    tri = turtle.getturtle()    # 下文中的 tri(默认的)第一个Turtle实例对象，可以将所有的tri替换成turtle,比如tri.lt(100) 可改成 turtle.lt(100)
    # 设置tri的(海龟箭头和)画笔大小的缩放模式为auto,此模式下(海龟箭头和)画笔随 pensize变化而变化.
    tri.resizemode("auto")
    # 创建一个新的Turtle实例对象并返回该对象实例
    turtle1 = turtle.Turtle()
    # 设置turtle1的(海龟箭头和)画笔大小的缩放模式为auto,此模式下(海龟箭头和)画笔随 pensize变化而变化.
    turtle1.resizemode("auto")
    # turtle1的海龟箭头图标设置成海龟
    turtle1.shape("turtle")
    turtle1.reset()
    turtle1.lt(90)
    # turtle1设置画笔速度为0最大速度
    turtle1.speed(0)
    # turtle1的画笔抬起
    turtle1.pu()
    # turtle1的画笔移动到坐标点(280, 40)
    turtle1.goto(280, 40)
    # turtle1的左转30度
    turtle1.lt(30)
    # turtle1的画笔放下
    turtle1.pd()
    # turtle1设置画笔速度为6
    turtle1.speed(6)
    # turtle1的pencolor设置成蓝色并且fillcolor设置成橘黄色
    turtle1.color("blue", "orange")
    # 设置画笔线条粗细为2, 同turtle.width(2)
    turtle1.pensize(2)
    # tri设置画笔速度为6
    tri.speed(6)
    # tri方向指向turtle1当前位置
    tri.setheading(tri.towards(turtle1))
    count = 1
    # 只要tri与turtle1之间距离>4像素进入循环
    while tri.distance(turtle1) > 4:
        turtle1.fd(3.5)
        turtle1.lt(0.6)
        tri.setheading(tri.towards(turtle1))
        tri.fd(4)
        if count % 20 == 0:
            # 当前位置拷贝一份turtle1实例的当前海龟箭头图标
            turtle1.stamp()
            # 当前位置拷贝一份tri实例的当前海龟箭头图标
            tri.stamp()
            # tri间断效果
            switchpen(tri)
            # turtle1间断效果
            #switchpen(turtle1)
        count += 1
    tri.write("CAUGHT! ", font=("Arial", 16, "bold"), align="right")
    tri.pencolor("black")
    tri.pencolor("red")

    # 等待2秒
    time.sleep(2)

    # 此处的turtle.undobufferentries()等价于turtle.getturtle().undobufferentries()或tri.undobufferentries()表示只要第一个turtle实例可以撤销,就一直撤销,因为tri的操作数量相对于turtle1要多,为了两个对象都撤销完所以用了前者
    while turtle.undobufferentries():
        # tri对象撤销一步
        tri.undo()
        # turtle1对象撤销一步
        turtle1.undo()
    # tri对象向前移动50像素
    tri.fd(50)
    tri.write("  Click anywhere to exit!", font=("Courier", 12, "bold"))
    # 获取海龟屏幕TurtleScreen对象实例
    screen = turtle.getscreen()
    # 注册点击事件,点击海龟屏幕TurtleScreen任何位置,触发close_window函数
    screen.onclick(close_window)


def close_window(x, y):
    print("点击位置(", x, ",", y, ")")
    # 获取当前海龟屏幕TurtleScreen的对象实例
    screen = turtle.getscreen()
    # 清屏
    screen.clearscreen()
    # 关闭窗口
    screen.bye()


def my_main():
    demo1()
    demo2()
    # 保持屏幕,直到点击窗口右上角关闭按钮或调用turtle.bye()方法
    turtle.mainloop()


if __name__ == '__main__':
    my_main()