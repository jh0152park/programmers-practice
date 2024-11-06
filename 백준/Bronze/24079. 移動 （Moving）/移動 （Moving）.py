import sys


x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())
z = int(sys.stdin.readline().strip())

if x + y <= z + 0.5:
    print("1")
else:
    print("0")