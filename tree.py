import turtle as t
import math
import time
def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)

def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)

def polygon(t, n, length):
	angle = 360.0/n
	polyline(t, n, length, angle)

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * abs(angle) / 360
	n = int(arc_length / 4) + 1
	step_length =arc_length / n
	step_angle = float(angle) / n

	t.lt(step_angle/2)
	polyline(t, n, step_length, step_angle)
	t.rt(step_angle/2)

def circle(t, r):
	arc(t, r, 360)


def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
	#Draws an Archimedian spiral starting at the origin
 
	theta = 0.0
 
	for i in range(n):
		t.fd(length)
		dtheta = 1 / (a + b * theta)
 
		t.lt(dtheta)
		theta += dtheta
 
#create the world and bob
#bob = turtle.Turtle()

 

if __name__ == '__main__':
	radius = 100
	t.pu()
	t.fd(radius)
	t.lt(90)
	t.pd()
	circle(t, radius)

	length = 100
	square(t, length)

	draw_spiral(t, n=1000)

	t.mainloop()

t.pu()

t.goto(50,50)
t.pd()
t.circle(50,steps=3)

#t.home()
t.color("red", "yellow")
#t.fillcolor("red")
t.speed(10)
# t.pu()
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(170)

t.end_fill()
t.pu()
t.goto(0,0)
t.pd()
t.write("菊花", font=('Arial', 40, 'normal'))

t.goto(-200,-200)
t.fd(100) #向前走
t.bk(100) #向后走

t.lt(90) #向左转
t.rt(90) #向右转

t.pu() #(pen up)抬笔
t.pd() #(pen down)落笔

t.mainloop()
t.done()
