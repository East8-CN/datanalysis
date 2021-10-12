# 定义一个函数 sum_numbers
# 能够接收一个 num 的整数参数
# 计算 1 + 2 + + ... num的结果
def sum_numbers(num):
    total = 0
    while num >= 1:
        total += num
        num -= 1
    print("%d %d" % (num, total))


def sum_numbers2(num):
    # 出口
    if num == 1:
        return 1
    # 数字的累加 num + (1 ... num - 1)
    temp = sum_numbers2(num - 1)
    return num + temp


result = sum_numbers2(1)
print(result)
