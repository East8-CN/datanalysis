# coding = utf-8
import os
import os.path


def visitDir1(path):
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        print(sub_path, type(sub_path))
        if os.path.isdir(sub_path):
            visitDir1(sub_path)


def visitDir2(path):
    list_dir = os.walk(path)
    for root, dirs, files in list_dir:
        for d in dirs:
            print(os.path.join(root, d))
        for file in files:
            print(os.path.join(root, file))


def visitDir3(arg, dirname, names):
    print('$arg' * 20)
    print(arg)
    print('$dirname' * dirname)
    print('$names' * 20)
    print(names)
    for filepath in names:
        print(os.path.join(dirname, filepath))


if __name__ == "__main__":
    # print("**************  call visitDir1  *******************")
    # visitDir1("D:\CODE\python\\file\\test")
    # print("**************  call visitDir2  *******************")
    # visitDir2("D:\CODE\python\\file")
    print("**************  call visitDir3  *******************")
    os.path.walk("D:\CODE\python\\file\\test", visitDir3, 1)
