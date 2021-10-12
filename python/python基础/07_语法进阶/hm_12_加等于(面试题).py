def demo(num, num_list):
    print("函数开始")
    num += num
    # 列表中变量使用 + 不会做相加再赋值的操作 !
    num_list = num_list + num_list
    # 本质上是在调用列表中的extend方法
    # num_list += num_list
    # num_list = num_list.extend(num_list)
    print(num)
    print(num_list)
    print(id(num_list))
    print("函数结束")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
print(id(gl_list))