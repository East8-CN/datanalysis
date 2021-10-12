import datetime
import random
temp = [i + 1 for i in range(35)]
random.shuffle(temp)
print(temp)
i = 0
list = []
while i < 7:
    list.append(temp[i])
    i = i + 1
list.sort()
print('\033[0;31;47m', end="")
print(*list[0:6], end="")
print('\033[0;38;42m', end=" ")
print(list[-1])


