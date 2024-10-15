import sys


def F(x):
    return str(int(x[0]) * len(x))


num = sys.stdin.readline().strip()

prev = num
while len(num) != 1:
    num = F(num)
    prev = num

if num == prev:
    print("FA")
else:
    print("NFA")