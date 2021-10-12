# 定义全局变量
num = 10


def demo1():
    # 希望修改全局变量的值,使用glabal声明一下即可
    global num
    num = 99                           
    print("demo1 == >%d %d" % (num, id(num)))


def demo2():
    print("demo2 == >%d %d" % (num, id(num)))


demo1()
demo2()
