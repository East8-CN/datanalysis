# coding=utf-8
# 类是客观世界中事物的抽象,而对象是类实例化后的变量.

# 类名 首字母大写
class Car:
    price = 200000  # 定义雷属性

    def __init__(self, c):
        self.color = c  # 定义实例属性


if __name__ == "__main__":
    car1 = Car("red")
    car2 = Car("blue")
    print(car1.color, Car.price)
    Car.price = 1500000  # 修改雷属性
    Car.name = "minicooper" # 增加类属性

    car1.color = "yello"  # 修改实例属性
    print(car2.color, Car.price, Car.name)
    print(car1.color, Car.price, Car.name)
