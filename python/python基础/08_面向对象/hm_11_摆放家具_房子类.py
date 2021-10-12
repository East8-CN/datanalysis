class House_item:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具[ %s ]占地面积 [%.2f]" % (self.name, self.area)


class House:
    def __init__(self, house_type, total_area):
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area
        self.item_list = []

    def __str__(self):
        return ("户型:[ %s ]总面积:[ %.2f ]平米剩余面积是:[ %.2f ]平米房屋家具有: %s "
                % (self.house_type, self.total_area, self.free_area, self.item_list))

    def add_item(self, house_item):
        # 1.判断要添加的家具占地面积是否大于可用面积,大于的话不能摆放,直接结束
        if house_item.area > self.free_area:
            print("家具[ %s ]占地面积太大,不能摆放" % house_item.name)
            return
        # 2.计算剩余面积
        self.free_area -= house_item.area
        # 3.添加家具
        self.item_list.append(house_item.name)


bed = House_item("席梦思", 40)
chest = House_item("柜子", 21)
table = House_item("桌子", 1.5)

house = House("两室一厅", 60)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)

# print(bed)
# print(chest)
# print(table)
