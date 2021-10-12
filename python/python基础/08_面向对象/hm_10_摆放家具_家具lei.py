class House_item:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具[ %s ]占地面积 [%.2f]" % (self.name, self.area)


bed = House_item("席梦思", 4)
chest = House_item("柜子", 2)
table = House_item("桌子", 1.5)

print(bed)
print(chest)
print(table)
