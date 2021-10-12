class Person:
    sex = 'mail'

    def __init__(self, s1, s2):
        self.IDcard = s1
        self.name = s2
        print('__init__(self) of person')

    def hello(self, friend):
        print('hello', friend, '!')


class Student(Person):
    def __init__(self, num):
        self.number = num

    def fun(self):
        print(self.IDcard, self.name, self.number, Student.sex)


class Teacher(Person):
    def __init__(self, t, s1, s2):
        self.title = t
        super(Teacher, self).__init__(s1, s2)
        # Person.__init__(self, s1, s2)

    def fun(self):
        print(self.IDcard, self.name, self.title, Teacher.sex)


if __name__ == "__main__":
    stu1 = Student('2021009')
    stu1.IDcard = '0001000010001'
    stu1.name = 'xiao ming'
    stu1.fun()
    stu1.hello("yang")

    teacher1 = Teacher('professer', '0010002002002', 'yangliping')
    Teacher.sex = 'femail'
    teacher1.fun()
    teacher1.hello("wang")
