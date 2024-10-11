n = int(input())

positions = []
for _ in range(n):
    x, y = map(int, input().split())
    positions.append((x, y))

positions.sort(key=lambda x:(x[0], x[1]))
for x, y in positions:
    print(x, y)