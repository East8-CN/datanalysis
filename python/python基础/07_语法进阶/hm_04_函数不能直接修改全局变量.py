# 定义全局变量
num = 10


def demo1():
    # 函数修改全局变量的值
    # 使用赋值语句会在函数内部定义一个局部变量的值

    num = 99
    print("demo1 == >%d %d" % (num, id(num)))


def demo2():
    print("demo2 == >%d %d" % (num, id(num)))


demo1()
demo2()
