import sys


a = 0
b = 0

a += int(sys.stdin.readline().strip()) * 3
a += int(sys.stdin.readline().strip()) * 2
a += int(sys.stdin.readline().strip()) * 1

b += int(sys.stdin.readline().strip()) * 3
b += int(sys.stdin.readline().strip()) * 2
b += int(sys.stdin.readline().strip()) * 1

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("T")