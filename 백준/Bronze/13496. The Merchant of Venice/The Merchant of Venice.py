import sys


tc = int(sys.stdin.readline().strip())

for t in range(tc):
    money = 0
    n, s, day = map(int, sys.stdin.readline().strip().split())
    for _ in range(n):
        d, v = map(int, sys.stdin.readline().strip().split())
        if s * day >= d:
            money += v

    print(f"Data Set {t + 1}:")
    print(f"{money}\n")