import os, os.path
filename = '2.txt'
rename = 'my.txt'

file_list = os.listdir('.')
print(file_list)
if filename in file_list:
    while(rename in file_list):
        choice = input("有重名,继续吗?[Y/N]")
        if choice in ['y', 'Y']:
            rename = input('请重新输入更新文件名:')
        else:
            break
    else:
        os.rename(filename, rename)
        print("重命名成功!")
else:
    print("需要更名的文件不存在!")
