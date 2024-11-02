import sys


n, u, l = map(int, sys.stdin.readline().strip().split())

if n >= 1000 and (u >= 8000 or l >= 260):
    print("Very Good")
elif n >= 1000 and not (u >= 8000 or l >= 260):
    print("Good")
else:
    print("Bad")