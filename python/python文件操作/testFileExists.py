import os.path
import os
a = os.path.exists('D:\\CODE\\python\\file\\1.txt')
print(a)
os.rename('D:\\CODE\\python\\file\\2.txt', 'D:\\CODE\\python\\file\\2.txt')
p = 'D:\\CODE\\python\\file\\2.txt'
os.path.dirname(p)
p2 = 'D:/CODE/python/file/2.txt'
os.path.split(p2)
os.path.splitdrive(p)
os.path.splitext(p)
