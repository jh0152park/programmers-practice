import sys


a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

if b * 7 + a <= 30:
    print("1")
else:
    print("0")