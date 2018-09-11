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
