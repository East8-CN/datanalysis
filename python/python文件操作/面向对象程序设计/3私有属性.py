# coding=utf-8
class Fruit:
    def __init__(self):
        self.__color = 'red'
        self.price = 2


if __name__ == "__main__":
    apple = Fruit()
    apple.price = 3
    print(apple.price, apple._Fruit__color)  # 访问私有属性
    apple._Fruit__color = "blue"  # 修改私有属性
    print(apple.price, apple._Fruit__color)

    peach = Fruit()
    print(peach.price, peach._Fruit__color)
