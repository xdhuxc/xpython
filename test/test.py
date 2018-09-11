#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 用来说明 Python 源程序文件使用的编码，默认情况下程序使用ASCII码。

a, b = 0, 1
while b < 1000:
    print(b),
    a, b = b, a+b

print

c = 0


def change_global(x):
    global c
    c = x
    print(c)


change_global(20)
print(c)

b1 = [1, 2, 3, 4]
b2 = [2, 4, 5, 7]
# 交集
b3 = [item for item in b1 if item in b2]
print(b3)
# 差集
b4 = [item for item in b1 if item not in b2]
print(b4)
