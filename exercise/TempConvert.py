#!/usr/bin/env python
# -*- coding: utf-8 -*-

temp_str = input("请输入带有符号的温度值：")
if temp_str[-1] in ['F', 'f']:
    c = (eval(temp_str[0:-1]) - 32) / 1.8
    print("转换后的温度是：{:.2f}C".format(c))
elif temp_str[-1] in ['C', 'c']:
    f = 1.8 * eval(temp_str[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(f))
else:
    print("输入格式错误。")


temp_str = input()
if temp_str[0] == "F":
    c = (eval(temp_str[1:]) - 32) / 1.8
    print("C{:.2f}".format(c))
elif temp_str[0] == "C":
    f = (eval(temp_str[1:]) * 1.8) + 32
    print("F{:.2f}".format(f))
else:
    print("输入格式错误。")

temp_str = input()
if temp_str[0:3] == "RMB":
    usd = eval(temp_str[3:]) / 6.78
    print("USD{:.2f}".format(usd))
elif temp_str[0:3] == "USD":
    rmb = eval(temp_str[3:]) * 6.78
    print("RMB{:.2f}".format(rmb))
else:
    print("输入格式错误。")
