n, x = map(int, input().split())
a = list(map(int, input().split()))

less = []
for n in a:
    if n < x:
        less.append(n)

print(*less)