#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python 中使用线程有两种方式：
1、函数
2、使用类来包装线程对象

函数式：调用thread模块中的start_new_thread()函数来产生新线程，语法如下：
thread.start_new_thread(function, args[, kwargs])
参数说明：
function：线程函数
args：传递给线程函数的参数，必须是个tuple类型。
kwargs：可选参数

线程的结束一般依靠线程函数的自然结束，也可以在线程函数中调用thread.exit()，抛出SystemExit 异常，达到退出线程的目的·。
"""

import thread
import time


def print_time(thread_name, delay):
    """
    为线程定义一个函数
    :param thread_name:
    :param delay:
    :return:
    """
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s---%s' % (thread_name, time.ctime(time.time())))

try:
    thread.start_new_thread(print_time, ('thread-xdhuxc', 2))
    thread.start_new_thread(print_time, ('thread-yztc', 4))
except:
    print('Error：不能启动线程')


while 1:
    pass

"""
使用Threading模块创建线程：
使用Threading模块创建线程，直接从threading.Thread继承，然后重写__init__和run()方法。
"""

