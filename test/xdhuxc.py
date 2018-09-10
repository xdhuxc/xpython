#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
将列表转换为集合，再将集合转换为列表，利用集合的自动去重功能。简单快速。缺点是：使用set方法无法保证去重后的顺序。
"""
original_list = [6, 6, 6, 6, 6, 6, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result_list = list(set(original_list))
print(result_list)

"""
使用集合方式的同时保证顺序性
"""
result_list.sort(key=original_list.index)
print(result_list)

# 循环遍历法，繁琐，不够简洁。
new_list = []
for item in original_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)
