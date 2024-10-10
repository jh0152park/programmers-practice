n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    print("%s BRAINS"%("MMM" if x >= y else "NO"))