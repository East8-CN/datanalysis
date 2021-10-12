from ysfcz import Vector2

v1 = Vector2(1, 2)
v2 = Vector2(3, 4)
v3 = (v1 + v2) / 2
v4 = v1 - v2
print(v1)
print(v2)
print(v3)
print(v4)
t = v4/3.0
t = t.getpos()
print (t[0], t[1])
