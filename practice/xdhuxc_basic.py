#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

'''
对已经加载的模块进行重新加载，一般用于原模块有变化等特殊情况，reload前该模块必须已经import过。
reload会重新加载已加载的模块，但原来已经使用的实例还是会使用旧的模块，而新生产的实例会使用新的模块；
reload后还是用原来的内存地址；
不能支持from * import * 格式的模块进行重新加载。
'''
reload(sys)
sys.setdefaultencoding('utf-8')

# 含前不含后，，默认步长为：1
for i in range(1, 5):
    print(i)

total_size = 0L


def get_dir_size(base_dir):
    global total_size
    xdhuxc_dir = unicode(base_dir)
    if not os.path.exists(xdhuxc_dir):
        print("%s 不存在。" % xdhuxc_dir)
        return None

    for item in os.listdir(xdhuxc_dir):
        full_path = os.path.join(xdhuxc_dir, item)
        print(full_path)
        if os.path.isfile(full_path):
            total_size = total_size + os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            get_dir_size(full_path)
    return total_size


def get_dir_size_xdhuxc(base_dir):
    global total_size
    xdhuxc_dir = unicode(base_dir)

    if not os.path.exists(xdhuxc_dir):
        print('%s 不存在。' % xdhuxc_dir)
        return -1

    for root, dirs, files in os.walk(xdhuxc_dir):

        for xfile in files:
            xdhuxc_file = unicode(xfile)
            full_path = os.path.join(root, xdhuxc_file)
            total_size = total_size + get_dir_size_xdhuxc(xdhuxc_file)

    return total_size

"""
在 Python 中，False, 0, '', [], {}, ()都可以视为假。
"""

"""
__name__ 是标识模块的名字的一个系统变量，这里分两种情况：
1、假如当前模块是主模块，也就是调用其他模块的模块，那么此模块的名字就是__main__，通过if判断这样就可以执行"__main__"后面的主函数内容
2、假如此模块是被import的，则此模块名字为文件名称（不加文件全名后面的.py），通过if判断就可以跳过"__main__"后面的内容。

通过这种方式，python就可以分清楚哪些是主函数，进入主函数执行，并且可以调用其他模块的各个函数等等。
"""

if __name__ == '__main__':
    xdhuxc = '123K'
    print(type(int(xdhuxc[:-1])))

    total_size = 0L
    src_dir = 'C:\\Users\\Administrator\\Desktop\yztc'
    #print(get_dir_size(src_dir))
    #print(get_dir_size_xdhuxc(src_dir))
    sys.getdefaultencoding()
    print(__filename__)
