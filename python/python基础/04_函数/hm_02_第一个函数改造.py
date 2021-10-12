# 可以由字母数字下划线组成
# 不可以由数字开头
# 不能与关键词崇明
# 定义好这个函数只表示这个函数封装了一段代码,如果不调用不能主动执行
"""
函数注释
"""
name = "小明"


def say_hello():
    """打招呼"""
    print("Hello python")
    print("Hello python")
    print("Hello python")


print(name)
# 只有在程序中主动调用函数,才会让函数执行
say_hello()
print(name)
