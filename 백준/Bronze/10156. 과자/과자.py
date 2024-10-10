cost, n, money = map(int, input().split())

need = cost * n

if money >= need:
    print("0")
else:
    print(need - money)