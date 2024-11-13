import sys


n = int(sys.stdin.readline().strip())
for i in range(n):
    a, b = map(float, sys.stdin.readline().strip().split())
    print("%.1f"%(abs(a - b)))