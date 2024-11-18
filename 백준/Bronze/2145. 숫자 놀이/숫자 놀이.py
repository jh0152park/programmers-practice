import sys


def compress(num):
    while num > 9:
        s = 0
        while num:
            s += num % 10
            num //= 10
        num = s
    return num


while True:
    num = int(sys.stdin.readline().strip())
    if not num:
        break
    print(compress(num))