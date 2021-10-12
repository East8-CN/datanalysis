# print("*"*50)
# print("1.新建名片")
# print("2.显示全部")
# print("3.查询名片")
# print()
# print("4.退出系统")
# print("*"*50)
# int(input("请输入您想要进行的操作: "))
import cards_tools
"""
本节知识点
1.字符串的判断
2.pass关键词的使用
3.无限循环

"""
while True:
    # TODO (小明)显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：　")
    print("您选择的操作是[%s] " % action_str)

    # TODO 123针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.card_add()
        # 显示全部
        elif action_str == "2":
            cards_tools.card_show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.card_show_one()
        # pass
    # 退出系统0
    elif action_str == "0":
        # 如果在开发程序时,不希望立刻编写执行代码
        # 可以在内部使用pass关键字,表示一个占位符,保证程序的结构代码正确
        # 程序运行时pass关键字不会执行任何的操作
        print("欢迎再次使用[名片管理系统]")
        break
        # pass
    # 其他内容输入错误

    else:
        print("您输入的不正确,请重新输入: ")
