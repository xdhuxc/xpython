#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = eval(input("请输入待计算的底数："))
if isinstance(n, int):
    power0 = 1
elif isinstance(n, float):
    power0 = 1.0
else :
    print("输入数据类型错误。")
print(power0, end=" ")
result = 1
for i in range(1, 6):
    result = n * power0 * result
    print(result, end=" ")

print()
print("=======================================")

power1 = n * power0
power2 = n * power1
power3 = n * power2
power4 = n * power3
power5 = n * power4
print(power0, power1, power2, power3, power4, power5)

print("+++++++++++++++++++++++++++++++++++++++")

for i in range(6):
    print(pow(n, i), end=" ")

print()
print("---------------------------------------")

for i in range(5):
    print(pow(n, i), end=" ")
print(pow(n, 5))

# print("", end=" ")
