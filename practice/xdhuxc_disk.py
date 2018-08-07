#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess


def uname():
    uname = 'uname'
    uname_arg = '-a'
    print('执行命令为：%s' % uname)
    xdhuxc = subprocess.call([uname, uname_arg])
    print(type(xdhuxc))


def disk():
    diskspace = 'df'
    diskspace_arg = '-h'
    print("执行命令为：%s" % diskspace )
    xdhuxc = subprocess.call([diskspace, diskspace_arg])
    print(type(xdhuxc))

uname()


disk()