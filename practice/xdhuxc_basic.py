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
        return None

    for root, dirs, files in os.walk(xdhuxc_dir):
        for xfile in files:
            full_path = os.path.join(root, xfile)
            total_size = total_size + os.path.getsize(full_path)
    return total_size

"""
       
            
    
"""

"""
在 Python 中，False, 0, '', [], {}, ()都可以视为假。
"""

if __name__ == '__main__':

    #total_size = 0L
    src_dir = 'C:\\Users\\wanghuan\\Desktop\\电子书'
    #print("get_dir_size: %d" % get_dir_size(src_dir))
    print("get_dir_size_xdhuxc: %d" % get_dir_size_xdhuxc(src_dir))
