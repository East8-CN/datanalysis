# coding = UTF-8
import pickle

f = open("D:\CODE\python\project\游戏项目开发\飞机大战\\2.dat", "wb")
n = 7
i = 13000
a = 99.6
s = '中国人民123abc'
lit = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tu = (-1, 2, 3)
coll = {4, 5, 6}
dic = {'a': 'apple', 'b': 'banana', 'o': 'orange'}
try:
    pickle.dump(n, f)
    pickle.dump(i, f)
    pickle.dump(a, f)
    pickle.dump(s, f)
    pickle.dump(tu, f)
    pickle.dump(coll, f)
    pickle.dump(dic, f)
except:
    print('写文件异常')
f.close()
