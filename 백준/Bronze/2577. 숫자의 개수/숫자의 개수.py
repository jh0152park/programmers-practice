a = int(input())
b = int(input())
c = int(input())

ret = str(a * b * c)
for i in range(10):
    print(ret.count(str(i)))