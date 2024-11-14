import sys

a = 0
b = 0
n = int(sys.stdin.readline().strip())

for _ in range(n):
    na, nb = map(int, sys.stdin.readline().strip().split())
    if na < a or nb < b:
        print("no")
        exit(0)
    a = na
    b = nb

print("yes")