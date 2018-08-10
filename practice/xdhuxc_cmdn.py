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
    with open('/proc/meminfo') as men_info:
        for line in men_info:
            if len(line) < 2:
                continue
            # 通过指定分隔符对字符串进行切片，默认为：默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
            memory_key = line.split(':')[0]
            memory_value = line.split(':')[1].split()[0]
            memory[memory_key] = long(memory_value) * 1024.0

    memory['MemUsed'] = memory['MemTotal'] - memory['MemFree'] - memory['Buffers'] - memory['Cached']
    # 计算内存使用率等
    memory['used_percent'] = format(float(memory['MemUsed']) / float(memory['MemTotal']), '.2f')
    return memory


def cpu_hardware_stat():
    """
    获取CPU相关信息
    :return:
    """
    cpu_hardware = []
    per_cpu = {}
    with open('/proc/cpuinfo') as cpu_hardware_info:
        for line in cpu_hardware_info:
            if line == '\n':
                cpu_hardware.append(per_cpu)
                per_cpu = {}
            if len(line) < 2:
                continue
            cpu_hardware_key = line.split(':')[0].rstrip()  # 删除字符串末尾指定的字符，默认为空格。
            cpu_hardware_value = line.split(':')[1]
            per_cpu[cpu_hardware_key] = cpu_hardware_value

    return cpu_hardware


# 参考资料
# http://www.blogjava.net/fjzag/articles/317773.html
def cpu_use_stat():

    print()


def load_average():
    load_average = {}
    with open('/proc/loadavg') as xfile:
        for line in xfile:
            # 系统在过去1分钟内运行队列中的平均进程数
            load_average['load_average_1'] = line.split()[0]
            # 系统在过去5分钟内运行队列中的平均进程数
            load_average['load_average_5'] = line.split()[1]
            # 系统在过去15分钟内运行队列中的平均进程数
            load_average['load_average_15'] = line.split()[2]
            # 正在运行的进程数
            load_average['running_process_number'] = line.split()[3].split('/')[0]
            # 进程总数
            load_average['total_process_number'] = line.split()[3].split('/')[1]
            # 最近运行的进程ID号
            load_average['last_pid'] = line.split()[4]
    return load_average


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
    free_disk_space = disk_info.f_bsize * disk_info.f_bfree
    disk_dir['free_disk_space'] = free_disk_space
    used_disk_space = total_disk_space - free_disk_space
    disk_dir['used_disk_space'] = used_disk_space
    # 保留两位小数
    disk_dir['used_percent'] = format(float(used_disk_space) / float(total_disk_space), '.2f')
    disk_dir['free_percent'] = format(float(free_disk_space) / float(total_disk_space), '.2f')
    return disk_dir


def readable(file_size):
    file_size = float(file_size)
    """
    以可视化的形式显示文件和目录大小。
    :param file_size:
    :return:
    """
    # 此处待优化
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


def test_disk_stat(path):
    disk_info = disk_stat(path)
    total_disk_space = readable(disk_info['total_disk_space'])
    free_disk_space = readable(disk_info['free_disk_space'])
    used_disk_space = readable(disk_info['used_disk_space'])
    used_percent = disk_info['used_percent']
    free_percent = disk_info['free_percent']
    print('total_disk_space: %s' % total_disk_space)
    print('free_disk_space: %s' % free_disk_space)
    print('used_disk_space: %s' % used_disk_space)
    print('used_percent: %s' % used_percent)
    print('free_percent: %s' % free_percent)


def test_memory_stat():
    memory_info = memory_stat()
    print('内存总量：%s' % readable(memory_info['MemTotal']))
    print('已使用内存：%s' % readable(memory_info['MemUsed']))
    print('空余内存：%s' % readable(memory_info['MemFree']))
    print('Buffers：%s' % readable(memory_info['Buffers']))
    print('Cached：%s' % readable(memory_info['Cached']))
    print('可用内存：%s' % readable(memory_info['MemAvailable']))
    print('内存使用率：%s' % memory_info['used_percent'])


def test_load_average():
    load_avg = load_average()
    load_average_1 = load_avg['load_average_1']
    print('过去1分钟的平均进程数：%s' % load_average_1)
    print('过去5分钟的平均进程数：%s' % load_avg['load_average_5'])
    print('过去15分钟的平均进程数：%s' % load_avg['load_average_15'])
    print('正在运行的进程数：%s' % load_avg['running_process_number'])
    print('进程总数：%s' % load_avg['total_process_number'])
    print('最后一个运行的进程ID：%s' % load_avg['last_pid'])
    cpu_hardware = cpu_hardware_stat()
    print('每一核CPU在过去1分钟内的负载：%.4f' % (float(load_average_1) / float(len(cpu_hardware))))


if __name__ == '__main__':
    """
    检测以下指标：
    1、CPU使用率
    2、内存使用率，超过80%报警，从memory_stat()获取的字典中取值判断
    3、平均负载过高报警，从load_average()中获取负载信息，再从cpu_hardware_stat()中获取CPU信息，计算平均负载
    4、磁盘空间超过80%报警，从disk_stat()中获取指定目录下磁盘使用情况
    报警方式包括：
    ①、控制台
    ②、邮件
    ③、短信
    ④、微信接口
    """
    print('内存信息：')
    test_memory_stat()
    print('磁盘信息：')
    test_disk_stat('/data')
    test_disk_stat('/')
    print('负载信息：')
    test_load_average()
