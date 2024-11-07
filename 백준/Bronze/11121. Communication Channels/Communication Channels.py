import sys


n = int(sys.stdin.readline().strip())
for i in range(n):
    a, b = map(str, sys.stdin.readline().strip().split())
    if a == b:
        print("OK")
    else:
        print("ERROR")