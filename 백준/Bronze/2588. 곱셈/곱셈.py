a = int(input())
b = int(input())
c = a * b
while b:
    mod = b % 10
    b //= 10
    print(a * mod)
print(c)