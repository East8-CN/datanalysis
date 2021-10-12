#!/usr/bin/python
# coding=utf-8
"""
@author: ligen
@contact:1095223921@qq.com
@file: 8.摄氏温度转换为华氏温度.py
@time: 2021-10-11 16:40
"""
celsius = float(input("请输入摄氏温度:"))
# 计算华氏温度
fahreheit = (celsius * 1.8) + 32
print("%0.1f 转换为华氏温度为 %0.1f " % (celsius, fahreheit))
if __name__ == "__main__":
    pass
