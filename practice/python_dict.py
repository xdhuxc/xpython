#!/usr/bin/env python
# -*- coding: utf-8 -*-


xdhuxc_dict = {'a': '1', 'b': '2', 'c': '3'}
# 遍历 key 值
# 在使用上，for key in xdhuxc_dict 和 for key in xdhuxc_dict.keys()完全等价
for key in xdhuxc_dict:
    print(key + ' : ' + xdhuxc_dict[key])


for key in xdhuxc_dict.keys():
    print(key + ' : ' + xdhuxc_dict[key])

# 遍历 value 值
for value in xdhuxc_dict.values():
    print(value)

# 遍历字典项
for kv in xdhuxc_dict.items():
    print(kv)

# 遍历字典键值
# 在使用上，for key, value in xdhuxc_dict.items() 和for (key, value) in xdhuxc_dict.items() 完全等价
for key, value in xdhuxc_dict.items():
    print(key + '--->' + value)

for (key, value) in xdhuxc_dict.items():
    print(key + '--->' + value)

xdhuxc_dict.update({'d': '2'})
print(xdhuxc_dict)


xdhuxc_dict['wanghuan'] = '123456'
xdhuxc_dict['lalala'] = '156'
print(xdhuxc_dict)