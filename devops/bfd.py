#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import getopt
import time

reload(sys)
charset = os.environ.get('CHARSET') or 'utf-8'
sys.setdefaultencoding(charset)  # 为了解决目录和文件名中文编码问题，

# https://blog.csdn.net/beautygao/article/details/79231571
'''
http://andylin02.iteye.com/blog/1071448
http://www.runoob.com/python/python-command-line-arguments.html
https://www.cnblogs.com/saiwa/articles/5253713.html
'''
# 声明全局变量


def get_dir_size(base_dir):
    total_size = 0L
    base_dir = unicode(base_dir)
    # 如果文件不存在，直接返回
    if not os.path.exists(base_dir):
        print("%s 不存在" % base_dir )
        return None

    if os.path.isfile(base_dir):
        return os.path.getsize(base_dir)
    '''
    os.walk()是一个简单易用的文件、目录遍历器，可以帮助我们高效地处理文件、目录方面的问题。
    os.walk()函数的声明为：
    walk(top, topDown=True, onerror=None, followlinks=False)
    参数：
    top：所要遍历的目录的地址。
    topDown为真，则优先遍历top目录，否则优先遍历top的子目录，默认为：True。
    onerror：需要一个callable对象，当walk需要异常时，会调用。
    followlinks：如果为真，则会遍历目录下的快捷方式实际所指的目录，默认为：False

    os.walk 的返回值是一个生成器，也就是说我们需要不断地遍历它，来获得所有的内容。

    每次遍历的对象都返回的是一个三元组(root, dirs, files)
    root：所指的是当前正在遍历的这个目录本身的地址。
    dirs：一个list，当前目录下所有目录的名字，不包括子目录。
    files：一个list，当前目录下的所有文件的名字，不包括子目录中的文件。

    如果topDown参数为真，walk会遍历top目录，与top目录中的每一个子目录。
    '''

    for root, dirs, files in os.walk(base_dir):
        # 处理root目录下的所有文件
        for file_item in files:
            file_path = os.path.join(root, file_item)
            if os.path.exists(file_path):
                total_size = total_size + os.path.getsize(file_path)
    return total_size


def readable(file_size):
    file_size = float(file_size)
    """
    以可视化的形式显示文件和目录大小。
    :param file_size:
    :return:
    """
    k, m, g, t, p = float(1024), float(1024**2), float(1024**3), float(1024**4), float(1024**5)
    if file_size < k:
        return format(file_size, '.2f') + 'B'
    elif file_size < m:
        return format((file_size / k), '.2f') + 'KB'
    elif file_size < g:
        return format((file_size / m), '.2f') + 'MB'
    elif file_size < t:
        return format((file_size / g), '.2f') + 'GB'
    elif file_size < p:
        return format((file_size / t), '.2f') + 'TB'
    else:
        return format((file_size / p), '.2f') + 'PB'


def main(argv):
    # 指定查找目录，默认为当前目录。
    base_dir = os.getcwd()
    # 默认显示500M以上的文件和目录
    min_size = 500
    # 指定排序规则asc或desc，默认为：asc，即升序。
    sort_type = 'asc'
    # 指定查找类型，默认为：all，即查找所有的文件和目录，可选项为：all，file，dir
    xtype = 'all'

    try:
        opts, args = getopt.getopt(argv, 'dstSh', ['--size=', '--type=', '--sort=', '--help='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-d':
            base_dir = arg
        elif opt in ('-t', '--type='): # -t all 或 --type=file
            xtype = arg
        elif opt in ('-S', '--sort='):
            sort_type = arg
        elif opt in ('-s', '--size='):
            min_size = resolve(arg)
        else:
            print("非法参数")
            usage()

    file_dict, dir_dict = preprocess(base_dir)
    # 文件或目录最小大小处理
    file_size_dict = bfd_size(file_dict, min_size)
    dir_size_dict = bfd_size(dir_dict, min_size)
    # 排序处理
    sort_file_dict = bfd_size(file_size_dict, sort_type)
    sort_dir_dict = bfd_size(dir_size_dict, sort_type)
    # 类型处理
    if xtype == 'file':
        print_dict(sort_file_dict)
        sys.exit(0)
    elif xtype == 'dir':
        print_dict(sort_dir_dict)
        sys.exit(0)
    elif xtype == 'all':
        total_dict = dict(sort_file_dict, **sort_dir_dict)
        print_dict(total_dict)
        sys.exit(0)


def usage():
    print('usage：python bfd.py [options] ')


def bfd_sort(sort_dict, sort_type):
    """
    对传入的字典sort_dict进行排序，排序规则由sort_type指定。
    :param sort_dict:
    :param sort_type:
    :return: 排序后的字典
    """
    if sort_type == 'desc':
        reverse = True
    else:
        reverse = False
    """
    按值对字典排序，
    :param sort_dict:
    :return:
    """
    sorted_key_list = sorted(sort_dict, key=lambda x: sort_dict[x], reverse=reverse)
    return map(lambda x: {x: sort_dict[x]}, sorted_key_list)


def bfd_size(select_dict, min_size):
    """
    根据大小筛选文件和目录
    :param select_dict: 待瘦身的字典
    :param min_size: 最小大小
    :return: 瘦身后的字典
    """
    for key, value in select_dict.items():
        if value < min_size:
            select_dict.pop(key)
    return select_dict


def resolve(xsize):
    """
    解析文件或目录大小的字符串
    :param xsize: 表示文件或目录大小的字符串，默认为字节数，可能为：23k，23K，56m，47M，12T，36等
    :return: 以字节表示的文件或目录大小
    """
    print('解析字符串k，g，t等，返回字节数B')
    if xsize[-1] in ('k', 'K'):
        return 1024*int(xsize[:-1])
    elif xsize[-1] in ('m', 'M'):
        return 1024*1024*int(xsize[:-1])
    elif xsize(-1) in ('g', 'G'):
        return 1024*1024*1024*int(xsize[:-1])
    elif xsize(-1) in ('t', 'T'):
        return 1024*1024*1024*1024*int(xsize[:-1])
    else:
        return int(xsize)


def preprocess(base_dir):
    """
    计算每个文件和目录的大小，并分别存储到list中
    :param base_dir: 基础目录名称，也可能是文件
    :return: file_list，directory_list
    """
    file_dict = {}
    dir_dict = {}
    xdhuxc_dir = unicode(base_dir)
    for root, dirs, files in os.walk(xdhuxc_dir):
        for xfile in files:
            full_path = os.path.join(root, unicode(xfile))
            file_dict.update({full_path: get_dir_size(full_path)})
        for xdir in dirs:
            full_path = os.path.join(root, unicode(xdir))
            dir_dict.update({full_path: get_dir_size(full_path)})
    return file_dict, dir_dict


def print_dict(prinx_dict):
    """
    打印字典的键值
    :param print_dict:
    :return:
    """
    for key, value in prinx_dict.items():
        print(readable(value) + "   " + key)


def print_list(prinx_list):
    """
    打印列表的值，列表中的每一个元素为一个字典
    :param prinx_list:
    :return:
    """
    for item in prinx_list:
        for key, value in item.items():
            print(readable(value) + '   ' + key)


if __name__ == '__main__':
    start_time = time.time()

    """
    base_dir = 'E:\\bak'
    result = get_dir_size(base_dir)
    print(result)
    print(readable(result))
    print("Hello World")
    size(base_dir, 500)
    """
    min_size = 500 * 1024 * 1024
    sort_type = 'asc'
    base_dir = 'E:\\bak'
    file_dict, dir_dict = preprocess(base_dir)

    # 文件或目录最小大小处理
    file_size_dict = bfd_size(file_dict, min_size)
    dir_size_dict = bfd_size(dir_dict, min_size)

    # print_dict(file_size_dict)
    # print_dict(dir_size_dict)

    # 合并文件字典和目录字典
    total_dict = dict(file_size_dict, **dir_size_dict)

    # 排序处理
    sorted_list = bfd_sort(total_dict, sort_type)

    print_list(sorted_list)

    # total_dict = dict(sort_file_dict, **sort_dir_dict)
    # print_dict(total_dict)
    # main(sys.argv[1:])
    end_time = time.time()
    print('耗时%f 秒' % (end_time-start_time))

