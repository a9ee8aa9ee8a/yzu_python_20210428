# 1*1=1 1*2=2 .... 1*9=9
# 2*1=2 2*2=4 .... 2*9=18
# ...
# 9*1=9 9*2=18 .... 9*9=81
# x*y=z
for x in range(1, 10):
    for y in range(1, 10):
        z = x * y
        print("%2d*%-2d=%2d" % (x, y, z), end=" ")   # % = C#format +數:由右至左排 -數:有左至右排
    print()
n = int(input("請輸入乘法表 size: "))+1
for x in range(1, n):
    for y in range(1, n):
        z = x * y
        print("%2d*%-2d=%-3d" % (x, y, z), end=" ")
    print()
