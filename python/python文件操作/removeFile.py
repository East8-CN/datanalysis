import os, os.path
filename = 'D:\\CODE\\python\\file\\2.txt'
if os.path.exists(filename):
    os.remove(filename)
else:
    print('%s dose not exist!' %filename)
