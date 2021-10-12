# coding = utf-8

class Demo:
    def hello(self):
        print("hello world!")


if __name__ == "__main__":
    Instance1 = Demo()


    def hello2(self):
        print("hello again!")


    Demo.hello2 = hello2
    Instance1.hello()
    Instance1.hello2()

    @staticmethod
    def hello3():
        print("hello once more!")

    Demo.hello3 = hello3
    Demo.hello3()
