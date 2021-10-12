#!/usr/bin/python
# coding=utf-8
"""
@author: ligen
@contact:1095223921@qq.com
@file: 3.1计算负数或者复数的平方根.py
@time: 2021-10-11 14:32
"""
import cmath
num = int(input("请输入一个数字:"))
num_sqrt = cmath.sqrt(num)
print("{0} 的平方根为 {1:0.3f} + {2:0.3f}j".format(num, num_sqrt.real, num_sqrt.imag))
if __name__ == "__main__":
    pass
