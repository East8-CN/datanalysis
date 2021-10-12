def demo(num, *args, **kwargs):
    """
    :param num: 传递参数
    :param args: 传递 * 元祖
    :param kwargs:  传递 ** 字典
    """
    print(1)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="小明", age="19")
