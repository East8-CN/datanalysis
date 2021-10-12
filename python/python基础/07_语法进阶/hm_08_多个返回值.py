def measure():
    """测量温度和湿度"""
    print("测量开始")
    temp = 39
    wetness = 50
    print("测量结束")
    # 元祖可以包含多个返回值,因此可以使用元祖让函数一次返回多个值
    return temp, wetness


result = measure()

print(result)
print(type(result))
