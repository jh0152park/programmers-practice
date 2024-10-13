import sys

b = []
a = list(map(int, sys.stdin.readline().strip().split()))
c = list(map(int, sys.stdin.readline().strip().split()))

b.append(c[0]-a[2])
b.append(c[1]//a[1])
b.append(c[2]-a[0])

print(*b)