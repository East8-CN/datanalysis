import os
file_list = os.listdir('.')
print(file_list)
for filename in file_list:
    name_list = os.path.splitext(filename)
    print(name_list)
    if name_list[1] == '.html':
        newname = name_list[0] + '.htm'
        os.rename(filename, newname)
        print(filename + "更名为:" + newname)
