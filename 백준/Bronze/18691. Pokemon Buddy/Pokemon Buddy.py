import sys

km = {
    1: 1,
    2: 3,
    3: 5
}

n = int(sys.stdin.readline().strip())
for _ in range(n):
    g, c, e = map(int, sys.stdin.readline().strip().split())

    if c < e:
        print((e - c) * km[g])
    else:
        print("0")