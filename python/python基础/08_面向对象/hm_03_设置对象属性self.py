class Cat:
    def eat(self):

        # 哪一个对象调用的方法,self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("小猫爱喝水")


# 可以使用 .属性名 利用赋值语句就可以了

# 创建猫对象
tom = Cat()
tom.name = "Tom"
tom.drink()
tom.eat()
print(tom)

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)
