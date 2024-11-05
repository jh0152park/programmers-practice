import sys


t = int(sys.stdin.readline().strip())
candy = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().strip().split()))

if sum(times) >= t:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")