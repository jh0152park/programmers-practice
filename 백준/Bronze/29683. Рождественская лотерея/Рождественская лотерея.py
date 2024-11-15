import sys


n, a = map(int, sys.stdin.readline().strip().split())
payment = list(map(int, sys.stdin.readline().strip().split()))

lottery = 0
for pay in payment:
    lottery += pay // a

print(lottery)