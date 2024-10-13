a = int(input())
b = int(input())
c = a + b

a = 0
while c:
    a += 1
    c //= 10

print(a)