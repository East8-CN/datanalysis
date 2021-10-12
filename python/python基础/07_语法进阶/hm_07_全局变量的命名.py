# 注意在开发时,应该吧全局变量定义在所有的函数上方
# 然后就可以保证所有的函数都可以调用到全局变量
gl_num = 10
gl_title = "黑马程序员"
gl_name = "小明"


def demo():
    # 如果全局变量和局部变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线
    num = 99
    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)


demo()


