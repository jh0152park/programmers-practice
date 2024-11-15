import sys


def make_num(n):
    num = []
    for i in range(1, int(n) + 1):
        num.append(str(i))
    return "".join(num)


n = sys.stdin.readline().strip()
print(n[-1] if n == make_num(n[-1]) else "-1")