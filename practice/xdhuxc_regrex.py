#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wanghuan
# date: 2018-10-14
# description:

import re

line = 'xddxsgaaaasxaaaaaaxc@163'
# regular_exprission = '^xdhu.*153$'

regular_exprission = '.*(x.{2,5}x).*'
match_result = re.match(regular_exprission, line)
if match_result:
    print(match_result.group(1))
else:
    print('no result')
