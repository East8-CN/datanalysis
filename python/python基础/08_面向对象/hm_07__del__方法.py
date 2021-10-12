class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了 " % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)

    def __str__(self):
        return "我是小猫: %s" % self.name
    # tom是一个全局变量


tom = Cat("Tom")
print(tom)
str(tom)
# del 关键词可以删除一个对象
del tom

print("_" * 50)
