import os, os.path
file_list = os.listdir('.')
print(file_list)
for file_name in file_list:
    name_list = os.path.splitext(file_name)
    print(name_list)
    print(type(name_list))
