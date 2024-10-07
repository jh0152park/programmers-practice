cost = 0
price = int(input())
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    cost += a * b

if price == cost:
    print("Yes")
else:
    print("No")