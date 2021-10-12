#!/usr/bin/python
# coding=utf-8
"""
@author: ligen
@contact:1095223921@qq.com
@file: 5.求三角形的面积.py
@time: 2021-10-11 16:13
"""
a = float(input("输入三角形第一边长:"))
b = float(input("输入三角形第二边长:"))
c = float(input("输入三角形第三边长:"))
# 计算半周长
s = (a + b + c)/2
# 计算面积
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("三角形的面积为:%0.2f" % area)
if __name__ == "__main__":
    pass
