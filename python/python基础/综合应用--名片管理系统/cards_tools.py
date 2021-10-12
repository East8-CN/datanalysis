cards_list = []


def show_menu():
    """ 显示菜单 """
    print("*" * 50)
    print("欢迎使用[名片管理系统]v1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def card_add():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    card = {"name": input("请输入姓名: "), "phone": input("请输入电话: "), "qq": input("请输入qq号码: "), "age": input("请输入年龄: ")}
    cards_list.append(card)
    print(cards_list)


def card_show_all():
    """查询全部"""
    print("-" * 50)
    print("显示所有的名片")
    # 判断是否存在名片记录,如果没有提示用户并返回
    if len(cards_list) == 0:
        print("当前系统不存在任何记录,请使用新功能添加名片!")
        return
    # 打印表头
    for card_key in ["姓名", "电话", "qq", "年龄"]:
        print(card_key, end="\t\t\t")
    # 打印分割线
    print("")
    print("-" * 50)
    for card in cards_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t" % (card["name"],
                                                    card["phone"],
                                                    card["qq"],
                                                    card["age"]))
        print("")


def card_show_one():
    """查询名片"""
    print("-" * 50)
    print("搜索名片")
    # 提示用户要输入的姓名
    find_name = input("请输入要查找的姓名: ")
    for card in cards_list:
        if card["name"] == find_name:
            print("要查找的名片已存在")
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t" % (card["name"],
                                                        card["phone"],
                                                        card["qq"],
                                                        card["age"]))
            #    TODO 针对找到的名片进行修改和删除的操作 1.修改 2.删除 0.返回上级菜单
            deal_card(card)
            break
    else:
        print("抱歉没找到 %s" % find_name)


def deal_card(find_dict):
    print(find_dict)
    action_str = input("请选择要执行的操作"
                       "[1] 修改 [2] 删除 [0]返回上一级菜单: ")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话")
        find_dict["qq"] = input_card_info(find_dict["qq"], "姓名")
        find_dict["age"] = input_card_info(find_dict["age"], "年龄")
        print("修改名片成功")
    elif action_str == "2":
        cards_list.remove(find_dict)
        print("删除名片")


def input_card_info(dict_value, tip_message):
    # 提示用户输入内容
    result_str = input(tip_message)
    # 针对用户的输入进行判断,如果用户输入了内容直接返回结果
    if len(result_str) > 0:
        return result_str
    # 如果用户没有输入内容,则返回字典原有的值
    return dict_value
