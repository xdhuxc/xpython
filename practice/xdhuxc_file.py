#!/usr/bin/env python
# -*- coding: utf-8 -*-


src = 'C:\\Users\\wanghuan\\Desktop\\temp.txt'
xdhuxc_file = open(src)
# 逐行读取文件
for line in xdhuxc_file:
    print(line),         # 在python 2.x版本中，使用“,”（不含双引号）可使输出不换行
print(xdhuxc_file)

print(xdhuxc_file.read(200))
"""
可以通过调用f.close()显式地关闭文件，一旦关闭了文件，该文件对象依然存在，但是无法再通过它来读取文件内容。
而且文件对象返回的可打印内容也表明文件已经被关闭。
"""
xdhuxc_file.close()

print(xdhuxc_file)

"""
with 语句对 xdhuxc_file文件对象调用在python中称为“上下文管理器”的方法，也就是说，它指定xdhuxc_file为指向文件内容
的新的文件实例。
在 with 打开的代码块内，文件是打开的，而且可以自由读取。但是，一旦python代码从with负责的代码段退出，文件会自动关闭。
"""
with open(src) as xdhuxc_file:
    for line in xdhuxc_file:
        print(line),

"""
在这段代码中，无论 with 中的代码块在执行的过程中发生任何情况，文件最终都会被关闭。
如果代码块在执行的过程中发生了一个异常，那么在这个异常被抛出前，程序会先将被打开的文件关闭。
"""
xdhuxc_file = open(src)
lines = xdhuxc_file.readlines() # 返回一个list，依次为文件中的每一行
print(lines)