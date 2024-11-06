import sys


n = int(sys.stdin.readline().strip())
for _ in range(n):
    no, a, b, c = map(int, sys.stdin.readline().strip().split())
    if a + b + c >= 55 and a >= 35 * 0.3 and b >= 25 * 0.3 and c >= 40 * 0.3:
            print(f"{no} {a + b + c} PASS")
    else:
        print(f"{no} {a + b + c} FAIL")