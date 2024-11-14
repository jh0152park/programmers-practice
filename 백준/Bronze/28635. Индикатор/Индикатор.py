import sys


m = int(sys.stdin.readline().strip())
a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

press = 0
while a != b:
    press += 1
    a += 1
    if a > m:
        a = 1

print(press)