# coding=utf-8
# python中类的析构函数是__del__,用来释放对象占用的资源,在python收回对象空间之前自动执行
# 如果用户设计析构函数,python将提供一个默认的析构函数
# 析构函数属于对象,每个对象都有自己的析构函数
class Car:
    def __init__(self, n):
        self.num = n
        print('编号为', self.num, '的对象出生了...')

    def __del__(self):
        print('编号为', self.num, '的对象死亡了')
