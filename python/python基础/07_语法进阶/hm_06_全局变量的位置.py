# 注意在开发时,应该吧全局变量定义在所有的函数上方
# 然后就可以保证所有的函数都可以调用到全局变量
num = 10


def demo():
    print("%d" % num)
    print("%s" % title)


# 再定义一个全局变量
title = "黑马程序员"

demo()
name = "小明"

# 编写代码原则
#  shellbang
#  import模块
#  定义全局变量
#  定义函数
#  执行代码
