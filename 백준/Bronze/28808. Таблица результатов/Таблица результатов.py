import sys


passed = 0
n, m = map(int, sys.stdin.readline().strip().split())
for _ in range(n):
    submited = sys.stdin.readline().strip()
    if submited.count("+") > 0:
        passed += 1

print(passed)