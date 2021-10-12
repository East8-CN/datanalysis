name = "测试分割线"


def print_line(char, times):
    """打印多行分隔符
    :param char:分割字符
    :param times: 分割次数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分割线
    :param char: 分割符
    :param times: 分隔符重复的次数
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1
