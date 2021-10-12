# 小明愛跑步
# 跑步體重減少1儘  吃饭体重增加0.5kg
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s 现在的体重是 %.2f kg" % (self.name, self.weight)

    def eat(self):
        self.weight = self.weight + 0.5

    def run(self):
        self.weight = self.weight - 1


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
