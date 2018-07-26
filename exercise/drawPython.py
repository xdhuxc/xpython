#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle
turtle.setup(650, 350, 200, 200)  # turtle.setup(width, height, startx, starty) 设置窗体大小及位置，不是必须的，默认在正中心
turtle.penup()    # 拾起画笔
turtle.fd(-250)
turtle.pendown()  # 放下画笔
turtle.pensize(25)
turtle.pencolor("purple")  # 设置颜色
turtle.seth(-40)     # turtle.setheading(single)
for i in range(4):
    turtle.circle(40, 80)   # circle(半径，角度)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40) # turtle.forward(d) d 可以为负值 向turtle的正前方向运行
# turtle.bk() 向turtle的反方向运行
turtle.circle(16, 180)  # 以turtle当前左侧的某个中心做曲线运行
turtle.fd(40 * 2 / 3)
turtle.done()  # 程序运行结束时不会自动退出，需要手动结束。

