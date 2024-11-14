import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    x, y, fold = map(int, sys.stdin.readline().strip().split())
    print(f"Data set: {x} {y} {fold}")
    for f in range(fold):
        if x > y:
            x //= 2
        else:
            y //= 2

    print(f"{max(x, y)} {min(x, y)}\n")