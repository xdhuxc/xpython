#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


exit_flag = 0


class XdhuxcThread(threading.Thread): # 继承父类threading.Thread

    def __init__(self, thread_id, thread_name, count):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.count = count

    def run(self):
        print('开始执行：' + self.thread_name)
        """
        获取锁，成功获得锁定后返回True，可选的timeout参数不指定时将一直阻塞直到获得锁定，否则超时后将返回False
        """
        thread_lock.acquire()
        print_time(self.thread_name, self.count, 10)
        # 释放锁
        thread_lock.release()
        print(self.thread_name + '执行结束')


def print_time(thread_name, delay, count):
    while count:
        if exit_flag:
            threading.Thread.exit()
        time.sleep(delay)
        print('%s---%s' % (thread_name, time.ctime(time.time())))
        count = count - 1


thread_lock = threading.Lock()

# 创建新线程
thread1 = XdhuxcThread(1, 'xdhuxc-thread', 2)
thread2 = XdhuxcThread(2, 'yztc-thread', 4)

# 启动线程
thread1.start()
thread2.start()


print('退出主线程。')

