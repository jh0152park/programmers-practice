import sys

n, m = map(int, sys.stdin.readline().strip().split())

if m <= 2:
    print("NEWBIE!")
elif m <= n and m > 2:
    print("OLDBIE!")
else:
    print("TLE!")