#!/usr/bin/python
# coding=utf-8
"""
@author: ligen
@contact:1095223921@qq.com
@file: 4.python计算二次方程平方根.py
@time: 2021-10-11 15:11
"""
"""
二次方程 ax**2 + bx + c = 0
a, b ,c ,用户提供,为实数,a != 0
"""
import cmath

a = float(input("请输入a:"))
b = float(input("请输入b:"))
c = float(input("请输入c:"))
# 计算
d = (b ** 2 - 4 * a * c)
# 两种求解方式
sol1 = (-b + cmath.sqrt(d)) / 2 * a
sol2 = (-b - cmath.sqrt(d)) / 2 * a
print("该方程的解为{0} 和 {1}".format(sol1, sol2))
if __name__ == "__main__":
    pass
