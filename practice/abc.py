#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def disk_stat(path):
    """
    posix.statvfs_result(f_bsize=4096, 文件系统块大小
                         f_frsize=4096, 分栈大小
                         f_blocks=6417977, 文件系统数据库总数
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
    disk_dir['free_disk_space'] = disk_info.f_bsize * disk_info.f_bfree
    used_disk_space = total_disk_space - free_disk_space
    disk_dir['used_disk_space'] = total_disk_space - free_disk_space
    disk_dir['used_percent'] = float(used_disk_space) / float(total_disk_space)
    disk_dir['free_percent'] = float(free_disk_space) / float(total_disk_space)
    return disk_dir


def readable(file_size):
    """
    以可视化的形式显示文件和目录大小。
    :param file_size:
    :return:
    """
    file_size = float(file_size)
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


if __name__ == '__main__':
    disk_info = disk_stat('/data')
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




