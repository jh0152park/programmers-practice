import sys


a, p = map(int, sys.stdin.readline().strip().split())
a *= 7
p *= 13

if a == p:
    print("lika")
elif a > p:
    print("Axel")
else:
    print("Petra")