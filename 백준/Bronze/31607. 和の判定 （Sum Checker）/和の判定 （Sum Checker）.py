import sys


a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

if a == b + c:
    print("1")
elif b == a + c:
    print("1")
elif c == a + b:
    print("1")
else:
    print("0")