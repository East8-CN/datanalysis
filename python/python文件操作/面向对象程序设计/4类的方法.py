# coding=utf-8
# 类的三种方法 公有方法,私有方法和静态方法
class Fruit:
    price = 0

    def __init__(self):
        self.__color = "red"
        self.__city = "kunming"

    def __outputColor(self):  # 定义私有方法
        print(self.__color)  # 访问私有属性

    def __outputCity(self):
        print(self.__city)

    def output(self):
        self.__outputColor()
        self.__outputCity()

    @staticmethod  # 定义静态方法
    def getPrice():
        return Fruit.price

    @staticmethod
    def setPrice(p):
        Fruit.price = p


if __name__ == "__main__":
    apple = Fruit()
    apple.output()
    print(Fruit.getPrice())
    Fruit.setPrice(9)
    print(Fruit.getPrice())