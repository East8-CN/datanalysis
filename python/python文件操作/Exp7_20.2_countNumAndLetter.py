f = open('D:\\CODE\\python\\file\\F7_15.txt', 'w')
s = '> Hi adjfkljadjfdfjald ceDd!@#$ a> jflasjdl'
f.write(s)
f.close()

f = open('D:\\CODE\\python\\file\\F7_15.txt', 'r')
nA = 0
na = 0
no = 0
nr = 0
while True:
    x = f.read(1)
    if x== '':
        break
    if x.isupper():
        nA = nA + 1
    elif x.islower():
        na = na + 1
    elif x.isdigit():
        n0 = n0 + 1
    else:
        nr = nr + 1
f.close()
print("nA = ", nA)
print("na = ", na)
print("no = ", no)
print("nr = ", nr)

        
