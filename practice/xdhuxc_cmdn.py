#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

# https://blog.csdn.net/huguangshanse00/article/details/17053789
# http://blog.51cto.com/dragonball/1413369
# https://blog.csdn.net/dearbaba_8520/article/details/80662181


def memory_stat():
    """
    用于计算内存占用状况
    :return: memory 字典，包含当前机器所有内存信息
    """
    memory = {}
    with open('C:\\Users\\wanghuan\\Desktop\\meminfo') as men_info:
        for line in men_info:
            # print(line),
            memory_key = line.split(':')[0]
            memory_value = line.split(':')[1].split()[0]
            memory[memory_key] = long(memory_value) * 1024.0

    memory['MemUsed'] = memory['MemTotal'] - memory['MemFree'] - memory['Buffers'] - memory['Cached']
    return memory


def cpu_stat():
    print()



if __name__ == '__main__':
    memory_info = memory_stat()
    for key, value in memory_info.items():
        print('%s ---> %d' % (key, value))