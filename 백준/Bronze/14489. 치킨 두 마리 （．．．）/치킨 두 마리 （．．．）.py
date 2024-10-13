import sys

m1, m2 = map(int, sys.stdin.readline().strip().split())
chicken = int(sys.stdin.readline().strip())

if m1 + m2 >= chicken * 2:
    print(m1 + m2 - (chicken * 2))
else:
    print(m1 + m2)