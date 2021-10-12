def demo(num, num_list):
    print("函数内部")
    print("赋值前num的值是:%d 地址是: %d" % (num, id(num)))
    num = 100
    num_list = [1, 2, 3]
    print("num的值是:%d 地址是: %d" % (num, id(num)))
    print(num_list)
    print("函数内部")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print("gl_num的值是:%d 地址是: %d" % (gl_num, id(gl_num)))
print(gl_list)
