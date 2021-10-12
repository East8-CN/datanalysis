def sum_number(num):
    print(num)
    # 递归函数出口很重要,否则就会陷入死循环
    if num == 1:
        return
    # 自己调用自己
    sum_number(num - 1)


sum_number(3)