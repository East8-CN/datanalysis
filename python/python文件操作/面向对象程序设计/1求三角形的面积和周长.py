# 类和对象
# 实例属性和类属性
# 类的方法
# 构造函数
# 西沟函数
# 运算符的重载
# 继承
# 求三角形的周长和面积
class Triangle:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1.0 / 2)

    def parameter(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    t1 = Triangle(6, 6, 6)
    t2 = Triangle(3, 4, 5)
    print("等边三角形的三条边: ", t1.a, t1.b, t1.c)
    print("等边三角形的面积: ", t1.area())
    print("等边三角形的周长: ", t1.parameter())

    print("直角三角形的三条边: ", t2.a, t2.b, t2.c)
    print("直角三角形的面积: ", t2.area())
    print("直角三角形的周长: ", t2.parameter())
