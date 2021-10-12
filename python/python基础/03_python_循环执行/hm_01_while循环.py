# 自然计数通常从1开始，程序计数通常从0开始
i = 0
total = 0
odd = 0
result = 0
while i <= 100:
    # print(i)
    if i % 2 == 0:
        print(i)
        odd = odd + i
    else:
        result = result + i
    total = total + i
    i = i + 1
print("0-100所有整数求和的值是: %d 0-100所有的偶数和是 %d 0-100的所有的奇数和是 %d" % (total, odd, result))
