#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# https://blog.csdn.net/huguangshanse00/article/details/17053789
# http://blog.51cto.com/dragonball/1413369
# https://blog.csdn.net/dearbaba_8520/article/details/80662181
# https://blog.csdn.net/huguangshanse00/article/details/17053891 含/proc/stat文件中参数含义
# https://blog.csdn.net/swiftshow/article/details/8109322 获取全部进程的资源信息


def memory_stat():
    """
    用于计算内存占用状况
    :return: memory 字典，包含当前机器所有内存参数及当前值信息，单位为：B。
    """
    memory = {}
    with open('C:\\Users\\wanghuan\\Desktop\\meminfo') as men_info:
        for line in men_info:
            # print(line),
            memory_key = line.split(':')[0] # 通过指定分隔符对字符串进行切片，默认为：默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
            memory_value = line.split(':')[1].split()[0]
            memory[memory_key] = long(memory_value) * 1024.0

    memory['MemUsed'] = memory['MemTotal'] - memory['MemFree'] - memory['Buffers'] - memory['Cached']
    return memory


def cpu_hardware_stat():
    cpu_hardware = []
    per_cpu = {}
    with open('') as cpu_hardware_info:
        for line in cpu_hardware_info:
            if line == '\n':
                cpu_hardware.append(per_cpu)
                per_cpu = {}
            cpu_hardware_key = line.split(':')[0].rstrip()  # 删除字符串末尾指定的字符，默认为空格。
            cpu_hardware_value = line.split(':')[1]
            per_cpu[cpu_hardware_key] = cpu_hardware_value

    return cpu_hardware


def cpu_use_stat():

    print()


def loadavg():
    load_avg = {}
    with open('/proc/loadavg') as xfile:
        for line in xfile:
            # 系统在过去1分钟内运行队列中的平均进程数
            load_avg['load_average_1'] = line.split()[0]
            # 系统在过去5分钟内运行队列中的平均进程数
            load_avg['load_average_5'] = line.split()[1]
            # 系统在过去15分钟内运行队列中的平均进程数
            load_avg['load_average_15'] = line.split()[2]
            # 正在运行的进程数
            load_avg['running_process_number'] = line.split()[3].split('/')[0]
            # 进程总数
            load_avg['total_process_number'] = line.split()[3].split('/')[1]
            # 最近运行的进程ID号
            load_avg['last_pid'] = line.split()[4]
    return load_avg


def disk_stat(path):
    """
    posix.statvfs_result(f_bsize=4096, 文件系统块大小
                         f_frsize=4096, 分栈大小
                         f_blocks=6417977, 文件系统数据块总数
                         f_bfree=4740020, 可用块数
                         f_bavail=4408244, 非root用户可获取的块数
                         f_files=1638400, 文件节点总数
                         f_ffree=1587583, 可用文件节点数
                         f_favail=1587583, 非root用户的可用文件节点数
                         f_flag=4096, 挂载标记
                         f_namemax=255) 最大文件长度
    :return:
    """
    disk_dir = {}
    disk_info = os.statvfs(path)
    total_disk_space = disk_info.f_bsize * disk_info.f_blocks
    disk_dir['total_disk_space'] = total_disk_space
    free_disk_space = disk_info.f_bsize * disk_info.f_bavail
    disk_dir['free_disk_space'] = disk_info.f_bsize * disk_info.f_bavail
    used_disk_space = disk_info.f_bsize * disk_info.f_bfree
    disk_dir['used_disk_space'] = disk_info.f_bsize * disk_info.f_bfree
    disk_dir['used_percent'] = float(used_disk_space) / total_disk_space
    disk_dir['free_percent'] = float(free_disk_space) / total_disk_space
    return disk_dir


def readable(file_size):
    """
    以可视化的形式显示文件和目录大小。
    :param file_size:
    :return:
    """
    k, m, g, t, p = 1024, 1024**2, 1024**3, 1024**4, 1024**5
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


if __name__ == '__main__':
    disk_info = disk_stat('/data')
    total_disk_space = readable(disk_info['total_disk_space'])
    free_disk_space = readable(disk_info['free_disk_space'])
    used_disk_space = readable(disk_info['used_disk_space'])
    used_percent = disk_info['used_percent']
    free_percent = disk_info['free_percent']
    print('total_disk_space: %d' % total_disk_space)
    print('free_disk_space: %d' % free_disk_space)
    print('used_disk_space: %d' % used_disk_space)
    print('used_percent: %d' % used_percent)
    print('free_percent: %d' % free_percent)