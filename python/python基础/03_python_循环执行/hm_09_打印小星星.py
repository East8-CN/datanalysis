# 在控制台连续输出五行*,每行星号的数量递增

row = 1
i = 5
while row <= i:
    print(((i-row)*" ")+(int(row*2) - 1)*"*")
    row += 1
