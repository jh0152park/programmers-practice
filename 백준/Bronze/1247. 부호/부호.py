import sys


for _ in range(3):
    n = int(sys.stdin.readline().strip())
    s = 0
    for _ in range(n):
        s += int(sys.stdin.readline().strip())

    if s == 0:
        print("0")
    elif s > 0:
        print("+")
    else:
        print("-")