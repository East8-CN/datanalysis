#!/usr/bin/python
# coding=utf-8
"""
@author: ligen
@contact:1095223921@qq.com
@file: 6.计算圆的面积.py
@time: 2021-10-11 16:18
"""
# 圆面积公式 S=pi*r**2  r为圆的半径
r = float(input("请输入圆的半径:"))


def findArea(a):
    PI = 3.142
    return PI * r * r


# 调用方法
print("圆的面积为 %.6f" % findArea(r))

if __name__ == "__main__":
    pass
